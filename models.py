from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Numeric
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
__tablename__ = "users"
id = Column(Integer, primary_key=True)
telegram_id = Column(String, unique=True)
username = Column(String)
created_at = Column(DateTime, default=datetime.utcnow)

class Invoice(Base):
__tablename__ = "invoices"
id = Column(Integer, primary_key=True)
user_id = Column(Integer, ForeignKey("users.id"))
inv_id = Column(String, unique=True)
amount = Column(Numeric)
status = Column(String, default="pending")
created_at = Column(DateTime, default=datetime.utcnow)
paid_at = Column(DateTime)

class Subscription(Base):
__tablename__ = "subscriptions"
id = Column(Integer, primary_key=True)
user_id = Column(Integer, ForeignKey("users.id"))
start_at = Column(DateTime)
end_at = Column(DateTime)
active = Column(Boolean, default=True)
