from twilio.rest import TwilioRestClient

account_sid = "AC105d60c624aa94795f785b3d678d4f07" # Your Account SID from www.twilio.com/console
auth_token  = "41a523311aa784cd10b05702b12f5a64"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Bot warning test",
    to="+86 188 0267 1838",    # Replace with your phone number
    from_="+16175443627") # Replace with your Twilio number

print(message.sid)