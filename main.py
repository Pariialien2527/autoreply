from telegram import *
from telegram.ext import *


bot =Bot("5352418616:AAFc9BNjRw1e4jLeQ2XdXZ-x8qtpD4azCPE")
#print(bot.get_me())
updater=Updater("53D4a52418616:AAFc9BNjRw1e4jLeQ2XdXZ-x8qtpD4azCPE",use_context=True)

dispatcher=updater.dispatcher

def test_function(update:Update,context:CallbackContext):
    bot.send_message(
	
	    chat_id=update.effective_chat.id,
		text="HI , I m the personal assistant of @khushi_2607",
		)


start_value=CommandHandler('motion_detection',test_function)

dispatcher.add_handler(start_value)


updater.start_polling()