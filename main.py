from twilio.rest import Client
import os

account_sid ='ACafaa6a04fcbb716aac08efe5979574c2'
auth_token ='1957567e3097a97fd2d49730404604a9'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Hello! Nice to meet you",
                    from_='+16105107302',
                    to='+91 9667206444'
                )

print(message.sid)