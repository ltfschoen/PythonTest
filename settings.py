# https://github.com/theskumar/python-dotenv
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

TEST_TWILIO_ACCOUNT_SID = os.environ.get("TEST_TWILIO_ACCOUNT_SID")
TEST_TWILIO_AUTH_TOKEN = os.environ.get("TEST_TWILIO_AUTH_TOKEN")
LIVE_TWILIO_ACCOUNT_SID = os.environ.get("LIVE_TWILIO_ACCOUNT_SID")
LIVE_TWILIO_AUTH_TOKEN = os.environ.get("LIVE_TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER") # Australia/Cocos/Christmas Island phone number can send and receive SMS
RECIPIENT_PHONE_NUMBER = os.environ.get("RECIPIENT_PHONE_NUMBER")