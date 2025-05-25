import logging
import asyncio
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from bot.handlers import handle_message
from bot.config import TELEGRAM_BOT_TOKEN

logging.basicConfig(level=logging.INFO)

async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
