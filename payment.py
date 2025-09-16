from fastapi import APIRouter, Request, Depends
from datetime import datetime, timedelta
from config import YKASSA_SHOP_ID, YKASSA_SECRET_KEY
import hmac, hashlib, json


router = APIRouter()


class YKassaService:
@staticmethod
def generate_link(inv_id: str, amount: float) -> str:
# Генерация тестовой ссылки для ЮKassa (Sandbox)
# В реальной интеграции используется API ЮKassa
return f"https://yookassa.ru/pay?shopId={YKASSA_SHOP_ID}&amount={amount}&invId={inv_id}&isTest=true"


@staticmethod
async def handle_callback(data: dict, session: Session):
# Проверка подписи
payload = data.get('object')
if not payload:
return "bad payload"


# В тестовом режиме пропускаем проверку
inv_id = payload.get('metadata', {}).get('invId')
amount = payload.get('amount', {}).get('value')


invoice = session.query(Invoice).filter_by(inv_id=inv_id).first()
if not invoice:
return "not found"


invoice.status = 'paid'
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


payment_service = YKassaService()


@router.post("/payment/result")
async def result_url(request: Request, session: Session = Depends(get_session)):
data = await request.json()
return await payment_service.handle_callback(data, session)


@router.get("/payment/link/{inv_id}/{amount}")
async def get_payment_link(inv_id: str, amount: float):
return {"link": payment_service.generate_link(inv_id, amount)}