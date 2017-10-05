from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)

call = client.calls.create(to=my_cell, from_=my_twilio, url="http://demo.twilio.com/docs/voice.xml")

print(call.sid)
