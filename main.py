import logging

from telegram import (Poll, ParseMode, KeyboardButton, KeyboardButtonPollType,
                      ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, PollAnswerHandler, PollHandler, MessageHandler,
                          Filters, ConversationHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

PODBOR = range(4)


def start(update, context):
    """Сообщите пользователю, что умеет этот бот"""
    update.message.reply_text(
        'Здоров, я Бот батан.\nМогу распидалить за цвевы для помощи в подборе выбери /podbor')

def podbor(update, context):
    reply_keyboard = [["Кадый день", "Через день", "Раз в неделю"]]
    update.message.reply_text(
        'Здоров, я Бот батан.\nМогу распидалить за цвевы'
        'Скажи как много времени ты готов уделять зеленым дармоедам?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    print(PODBOR)
    return PODBOR

def cancel(update, context):
    user = update.message.from_user
    logger.info("Пользователь %s завершил разговор.", user.first_name)
    update.message.reply_text('До свидания! Я надеюсь, что когда-нибудь мы сможем снова поговорить.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def main():

    updater = Updater('844125015:AAFnsQim1vBur-OTVphYy-MoQzKNAu2N3eI', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('podbor', podbor))


    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()