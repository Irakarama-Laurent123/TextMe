# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = '*********************************'
auth_token = '**********************************'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Python Powers Laurent.",
                     from_='+12183003053',
                     to='+250**********'
                 )

print(message.sid)
