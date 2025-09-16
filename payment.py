import hashlib
from fastapi import APIRouter, Request
from db import get_session
from models import Invoice, Subscription
from datetime import datetime, timedelta
from config import ROBO_PASS2

router = APIRouter()

@router.post("/payment/result")
async def result_url(request: Request, session=next(get_session())):
data = dict(await request.form())
out_sum = data.get("OutSum")
inv_id = data.get("InvId")
sign = data.get("SignatureValue")

base = f"{out_sum}:{inv_id}:{ROBO_PASS2}"
expected = hashlib.md5(base.encode()).hexdigest().upper()

if expected != sign.upper():
return "bad sign"

invoice = session.query(Invoice).filter_by(inv_id=inv_id).first()
if not invoice:
return "not found"

invoice.status = "paid"
invoice.paid_at = datetime.utcnow()

sub = Subscription(
user_id=invoice.user_id,
start_at=datetime.utcnow(),
end_at=datetime.utcnow() + timedelta(days=30),
active=True
)
session.add(sub)
session.commit()

return f"OK{inv_id}"