from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ["BOT_TOKEN"]  # Secure: token is read from environment

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💸 Welcome to MoneyPrinter! Type /print to start printing...")

async def print_money(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🖨 Printing money... 💰💰💰")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("print", print_money))
    print("Bot is running...")
    app.run_polling()
