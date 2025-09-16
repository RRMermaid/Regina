from apscheduler.schedulers.asyncio import AsyncIOScheduler
from db import get_session
from models import Subscription
from datetime import datetime
from telegram_bot import revoke_access

async def check_expired():
session = next(get_session())
now = datetime.utcnow()
expired = session.query(Subscription).filter(Subscription.end_at < now, Subscription.active==True).all()
for sub in expired:
sub.active = False
session.commit()
await revoke_access(sub.user_id)

def start_scheduler():
scheduler = AsyncIOScheduler()
scheduler.add_job(check_expired, "interval", hours=24)
scheduler.start()