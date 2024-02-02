from typing import final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


T: final = '6567480470:AAHSfwEOPyJ6W_1Ma-IrNA5e51iTQczVLhs'
BOT_USERNAME: final  =  '@White_Beard_bot'

async def start_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.massage.reply_text("Hello Boss")

async def help_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.massage.reply_text("I can do enything")

async def coustom_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.massage.reply_text("this is coustom")


def handle_respond(text: str):
    processed: str = text.lower()
    if '/start' in processed:
        return 'Welcome to ICT'
    if 'hello' in processed:
        return 'Hey There'
    if 'how are you' in processed:
        return 'Im goood'
    return 'i dont understand'




async def handle_massage(update: Update, contexttype: ContextTypes.DEFAULT_TYPE):
    massage_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {massage_type}: "{text}"')

    if massage_type == 'group':
        if BOT_USERNAME in text:
            new_text: str  =text.replace(BOT_USERNAME, '').strip()
            response: str = handle_respond(new_text)
        else:
            return
    else:
        response: str = handle_respond(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(T).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', coustom_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_massage))


    app.add_error_handler(error)


    print("Polling....")
    app.run_polling(poll_interval=3)






