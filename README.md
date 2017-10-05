# Simple-Twilio-SMS
Created by Kyle Lim

A Small little SMS test project using the Twilio API.

### Dependencies

Twilio Account (Premium for calls)

Phone Number

Python3 +

Twilio+
```sudo pip3 install twilio```

For receive_sms.py...

Flask
```sudo pip3 install flask```

ngrok 2.0+
```sudo apt-get install ngrok-client```
Or if not getting the latest version, go to ngrok website and put in /usr/bin

If on windows download ngrok.exe and run it from CMD. Bash on Windows does not
support networking tools such as ngrok.

### How to run

##### Send SMS

Simply add credential to credential.py file

Change message in the send_sms.py file

Run send_sms.py
```
python3 send_sms.py
```

##### Set up Receive Message Server

Change desired response message in receive_sms.py

```
python3 receive_sms.py
```

On another terminal run

```
ngrok http 5000
```

Go on the twilio website to your twilio phone number and add the forwarding
address to the messaging webhook.

##### Call Someone

Add credentials to credential.py file

Run make_call.py
```
python3 make_call.py
```

##### Respond to call

Change desired response message in receive_call.py

```
python3 receive_call.py
```

On another terminal run
```
ngrok http 5000
```

Go on the twilio website to your twilio phone number and add the forwarding
address to the call webhook.

