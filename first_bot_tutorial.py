import logging 
from telegram import Update 
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="I'm a bot. Please talk to me!")

if __name__ == "__main__":
    with open("telegram_api_token.txt") as f:
        api_token = f.readline().strip("\n")
    application = ApplicationBuilder().token(api_token).build() 

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    application.run_polling()