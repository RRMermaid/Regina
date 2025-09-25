import uvicorn
from fastapi import FastAPI
from payment import router as payment_router
from telegram_bot import dp, bot
from scheduler import start_scheduler
import asyncio


app = FastAPI()
app.include_router(payment_router)


@app.on_event("startup")
async def startup():
    start_scheduler()
    asyncio.create_task(dp.start_polling(bot))


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080)
