import logging 
from telegram import Update 
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler
# imports for inline queries
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="I'm a bot. Please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text=update.message.text)

async def caps(update:Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper() 
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text=text_caps)

async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)

async def inline_append_abc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    If the user enters this message:
    bbbHow are you? 
    Then the bot will return: 
    How are you?bbb 
    """
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query,
            title='Append abc',
            input_message_content=InputTextMessageContent(query[3:] + "abc")
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)


if __name__ == "__main__":
    with open("telegram_api_token.txt") as f:
        api_token = f.readline().strip("\n")
    application = ApplicationBuilder().token(api_token).build() 

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    caps_handler = CommandHandler("caps", caps)
    application.add_handler(caps_handler)

    # The pattern is detected using re.match, which means that the pattern 
    # is searched for at the *beginning* of the string. 
    inline_append_abc_handler = InlineQueryHandler(inline_append_abc, pattern="abc")
    application.add_handler(inline_append_abc_handler)

    inline_caps_handler = InlineQueryHandler(inline_caps)
    application.add_handler(inline_caps_handler)

    application.run_polling()