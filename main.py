import openai
import telegram
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update, context):
    await update.message.reply_text("Привет! Я GPT-бот. Напиши мне что-нибудь.")

async def handle_message(update, context):
    user_input = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Можно заменить на gpt-4, если у тебя есть доступ
        messages=[{"role": "user", "content": user_input}]
    )
    reply = response.choices[0].message.content
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()

