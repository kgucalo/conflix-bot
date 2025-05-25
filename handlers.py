from telegram import Update
from telegram.ext import ContextTypes
from bot.analyzer import analyze_text
from bot.responder import generate_responses
from bot.anonymizer import anonymize

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    anon = "анонимно" in text.lower()
    clean_text = anonymize(text) if anon else text

    analysis = analyze_text(clean_text)
    responses = generate_responses(clean_text, analysis)

    reply = "\n".join([f"{i+1}. {r}" for i, r in enumerate(responses)])
    await update.message.reply_text(f"🔍 Анализ: {analysis}\n\n💬 Варианты ответа:\n{reply}")
