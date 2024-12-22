import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Bot Token
TOKEN = '7672988832:AAFzhFBu1lfF3hEleokRFBw-dOR-UBSvYvc'  # আপনার বট টোকেন এখানে দিন

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Logo পাঠানোর ফাংশন
def send_logo(update: Update):
    # Google Drive থেকে লোগো লিঙ্ক
    logo_url = 'https://drive.google.com/uc?id=137LQJHaxZkvn3kBt5TC8ea1mxTdd1kIR'  # আপনার Google Drive লিঙ্ক দিন
    update.message.reply_photo(logo_url)

# Start Command Handler
def start(update: Update, context: CallbackContext) -> None:
    send_logo(update)  # লোগো পাঠান
    update.message.reply_text(
        'স্বাগতম! আমি রকির আব্বু Tu-Padre  আপনার অডিও/ভিডিও প্লেয়ার বট। আমাকে একটি অডিও বা ভিডিও ফাইল পাঠান এবং আমি সেটা চালিয়ে দিব।'
    )

# Help Command Handler
def help_command(update: Update, context: CallbackContext) -> None:
    send_logo(update)  # লোগো পাঠান
    update.message.reply_text('আমাকে একটি অডিও বা ভিডিও ফাইল পাঠান এবং আমি সেটা আপনার জন্য প্লে করব!')

# Play Audio
def play_audio(update: Update, context: CallbackContext) -> None:
    audio = update.message.audio
    if audio:
        send_logo(update)  # লোগো পাঠান
        update.message.reply_text(f'অডিও প্লে হচ্ছে: {audio.file_name}')
        update.message.reply_audio(audio.file_id)

# Play Video
def play_video(update: Update, context: CallbackContext) -> None:
    video = update.message.video
    if video:
        send_logo(update)  # লোগো পাঠান
        update.message.reply_text(f'ভিডিও প্লে হচ্ছে: {video.file_name}')
        update.message.reply_video(video.file_id)

# Handle incoming messages (audio/video)
def handle_message(update: Update, context: CallbackContext) -> None:
    if update.message.audio:
        play_audio(update, context)
    elif update.message.video:
        play_video(update, context)
    else:
        update.message.reply_text("অনুগ্রহ করে আমাকে একটি অডিও বা ভিডিও ফাইল পাঠান।")

# Main function to run the bot
def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Register message handler
    dispatcher.add_handler(MessageHandler(Filters.audio, play_audio))
    dispatcher.add_handler(MessageHandler(Filters.video, play_video))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
