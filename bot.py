import os
import requests

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'You could put any content here you like, perhaps even a homepage for your bot!'


@app.route('/', methods=['POST'])
def receive():
    data = request.get_json()
    print('Incoming message:')
    print(data)

    # Prevent self-reply
    if data['sender_type'] != 'bot':
        if data['text'].startswith('/ping'):
            message=data['name'] + ' pinged me!'
            print(message)
            send(message)

    return 'ok', 200


def send(msg):
    url  = 'https://api.groupme.com/v3/bots/post'
    print("trying to send something")
    data = {
          'bot_id' : os.getenv('BOT_ID'),
          'text'   : msg,
         }
    print(data)
    response = requests.post("https://api.groupme.com/v3/bots/post", json=data)
    print(response)