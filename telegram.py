import telegram.ext



Token = "tokenkey"

updater = telegram.ext._updater("",use_context= True) 
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hello world!")

def help(update,context):
    update.message.reply_text(
        """
        /start -> Welcome to the channel
        /help -> This particular message
        /content -> About various Playlists of SimpliLearn
        /Python -> The first video from the Python playlist
        /SQL -> The first video from the SQL playlist
        /Java -> The first video from the Java playlist
        /contact -> Contact information
        """
    )

def content(update,context):
    update.message.reply_text("We have various playlist and articles available")

def Python(update,context):
    update.message.reply_text("link : https://nischallamichhane.com.np")


def SQL(update,context):
    update.message.reply_text(" link: https://google.com")

def Java(update,context):
    update.message.reply_text(" link: https://google.com")

def contact(update,context):
    update.message.reply_text(" link: https://google.com")

dispatcher.add_handler(telegram.ext.CommandHandler('start',start))
dispatcher.add_handler(telegram.ext.CommandHandler('Python',Python))
dispatcher.add_handler(telegram.ext.CommandHandler('SQL',SQL))
dispatcher.add_handler(telegram.ext.CommandHandler('Java',Java))
dispatcher.add_handler(telegram.ext.CommandHandler('contact',contact))
dispatcher.add_handler(telegram.ext.CommandHandler('help',help))

updater.start_polling()
updater.idle()

