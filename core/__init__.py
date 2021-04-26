import os
import telebot
from dotenv import load_dotenv
from flask import (Flask, request, abort)
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

load_dotenv()


token = os.environ['TOKEN']
WEBHOOK_URL_BASE = os.environ['URL_PATH']
WEBHOOK_URL_PATH = token

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
bot = telebot.TeleBot(token, threaded=False)
manager.add_command('db', MigrateCommand)


# Configs
# ...
app.config['SECRET_KEY'] = os.environ['SECRET']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join('..') + '/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Bot API view
@app.route('/' + WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        abort(403)

# Custom views
# ...
