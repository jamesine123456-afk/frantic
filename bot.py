import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Setup logging for Railway logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Fetch your token from Railway Environment Variables
TOKEN = os.environ.get("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your Edu-Tool bot. Send me a topic, and I will summarize it for you.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    # Simple educational output structure
    response = (
        f"📚 *Topic:* {user_text}\n\n"
        f"🐣 *ELI5:* This is a foundational concept that helps us understand how things work in the real world.\n\n"
        f"📖 *Classroom:* A structured, academic look at the subject matter.\n\n"
        f"🔬 *Deep Dive:* Technical analysis involves complex variables and specific methodologies."
    )
    await update.message.reply_text(response, parse_mode='Markdown')

if __name__ == '__main__':
    # Build the application
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    # Run the bot
    application.run_polling()
