import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Загружаем переменные окружения из .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Твой сайт-магазин (замени на свой URL)
SHOP_URL = "https://yourshop.com"

# Функция обработки команды /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Привет! Я бот магазина. Используй /shop, чтобы перейти в магазин."
    )

# Функция обработки команды /shop
async def shop(update: Update, context: CallbackContext):
    await update.message.reply_text(f"🛒 Магазин: [Перейти в магазин]({SHOP_URL})", parse_mode="Markdown")

# Функция обработки сообщений
async def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()

    if text == "/shop":
        await shop(update, context)
    else:
        await update.message.reply_text("Я не понимаю этот запрос. Используйте /shop.")

# Основная функция для запуска бота
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("shop", shop))  # Добавили обработчик команды /shop
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
