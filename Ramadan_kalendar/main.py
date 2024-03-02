from telegram import Update, ForceReply
from telegram.ext import CommandHandler, Application, ContextTypes, MessageHandler, CallbackContext
from settings import settings

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!")


def main():
    application = Application.builder().token(settings.TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler('start', start))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


main()