import os
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from models.telegram_message import TelegramMessage
from modules.telebot_manager import telegram_bot
from datetime import datetime

app = FastAPI(docs_url=None, redoc_url=None)

ENABLED_RECIPIENTS_IDS = os.getenv("ENABLED_RECIPIENTS_IDS").split(",")

@app.get("/")
def read_root() -> str:
   return "No data!"

@app.post("/send-msg")
def send_msg(telegram_message: TelegramMessage) -> JSONResponse:
   if telegram_message.chat_id not in ENABLED_RECIPIENTS_IDS:
       return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
               "status": "error", 
               "message": "Recipient not enabled."
            }
       )

   bot_response = telegram_bot.send_message(telegram_message)
   return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
      "status": "success", 
      "message": telegram_message.dict(), 
      "bot_response": 
         {
            "date": str(datetime.fromtimestamp(bot_response.date)),
            "date_timestamp": bot_response.date,
            "message_id": bot_response.message_id, 
            "chat_id": bot_response.chat.id, 
            "text": bot_response.text
         }
      }
   )