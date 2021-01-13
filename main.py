from twilio.rest import Client
import os

account_sid ='aaaa'
auth_token ='xxxx'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Hello! Nice to meet you",
                    from_='+16105107302',
                    to='+91 9667206444'
                )

print(message.sid)