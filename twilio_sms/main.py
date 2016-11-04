import sys
import site
def get_main_path():
    app_path = sys.path[0] # sys.path[0] is current path in subdirectory
    split_on_char = "/"
    return split_on_char.join(app_path.split(split_on_char)[:-1])
main_path = get_main_path()
site.addsitedir(main_path)
site.addsitedir(main_path+'/util')
from util import python_version

print ( ("Importing main folder: {}".format(main_path)) if (python_version.current_version() == 3) else ("Importing main folder: %s") % (main_path) )

import settings

from twilio.rest import TwilioRestClient

account_sid = settings.LIVE_TWILIO_ACCOUNT_SID # Your Account SID from www.twilio.com/console
auth_token = settings.LIVE_TWILIO_AUTH_TOKEN  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account=account_sid, token=auth_token)

message = client.messages.create(body="Hello from Python",
                                 to=settings.RECIPIENT_PHONE_NUMBER, # Replace with your phone number
                                 from_=settings.TWILIO_PHONE_NUMBER) # Replace with your Twilio number
print(message.sid)