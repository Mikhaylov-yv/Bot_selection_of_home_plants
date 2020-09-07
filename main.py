import logging

from telegram import (Poll, ParseMode, KeyboardButton, KeyboardButtonPollType,
                      ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, PollAnswerHandler, PollHandler, MessageHandler,
                          Filters, ConversationHandler, CallbackQueryHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
UXOD, COLOR = range(2)

def start(update, context):
    """Сообщите пользователю, что умеет этот бот"""
    # update.send_photo(photo=open('zam.jpg', 'rb'))
    reply_keyboard = [["Кадый день", "Через день", "Раз в неделю"]]
    update.message.reply_text(
        'Здоров, я Бот батан.\nМогу распидалить за цвевы'
        'Скажи как много времени ты готов уделять зеленым дармоедам?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return UXOD

def color(update, context):
    reply_keyboard = [["Очень светло", "Средне", "Темноно как в пещере"]]
    update.message.reply_text(
        'Как у тебя в комнате с освещением',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return COLOR

def get_img_flow(update, context):
    context.bot.send_photo(chat_id = update.effective_chat.id,  photo=open('zam.jpg', 'rb'),
                           caption = 'Ваш лучший выбор: Замиокулькас')


def cancel(update, context):
    user = update.message.from_user
    logger.info("Пользователь %s завершил разговор.", user.first_name)
    update.message.reply_text('До свидания! Я надеюсь, что когда-нибудь мы сможем снова поговорить.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def main():

    updater = Updater('844125015:AAFnsQim1vBur-OTVphYy-MoQzKNAu2N3eI', use_context=True)

    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            UXOD: [MessageHandler(Filters.regex('^(Кадый день|Через день|Раз в неделю)$'), color)],
            COLOR: [MessageHandler(Filters.regex('^(Очень светло|Средне|Темноно как в пещере)$'), get_img_flow)]

        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)
    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()