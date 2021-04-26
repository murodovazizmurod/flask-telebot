import time

from core import (bot, app, WEBHOOK_URL_BASE, WEBHOOK_URL_PATH)


# Telegram Bot Code 

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello, World :)")


# Remove webhook
bot.remove_webhook()

time.sleep(0.1)

# Set webhook
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH)

if __name__ == "__main__":
    app.run(host=WEBHOOK_URL_BASE)
