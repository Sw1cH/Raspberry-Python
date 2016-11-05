from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )
import random

twitter = Twython(consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

messages = [
    "Hello world",
    "Hi there",
    "What's up?",
    "How's it going?",
    "Have you been here before?",
    "Get a hair cut!",
]

##message = random.choice(messages)
##twitter.update_status(status=message)
##print("Tweeted: %s" % message)

message = "Hello world - here's a picture!"
with open('/home/pi/Desktop/python projects/helloworld.jpg', 'rb') as photo:
    twitter.upload_media(status=message, media=photo)

