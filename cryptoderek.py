# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "jaysonbackes@gmail.com"
pas = "cGTpsL!dS3y2F"

sms_gateway = '6158098494@vtext.com'
# The server we use to send emails in our case it will be gmail but every email provider has a different smtp 
# and port is also provided by the email provider.
smtp = "smtp.gmail.com" 
port = 587
# This will start our email server
server = smtplib.SMTP(smtp,port)
# Starting the server
server.starttls()
# Now we need to login
server.login(email,pas)

# Now we use the MIME module to structure our message.
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = sms_gateway
# Make sure you add a new line in the subject
msg['Subject'] = "You can insert anything\n"
# Make sure you also add new lines to your body
body = "You can insert message here\n"
# and then attach that body furthermore you can also send html content.
msg.attach(MIMEText(body, 'plain'))

sms = msg.as_string()

server.sendmail(email,sms_gateway,sms)

# lastly quit the server


import cryptocompare

cryptocompare.cryptocompare._set_api_key_parameter('2722bd1e76ffa497594e310b4605e5aa7e1a1d7a79fef5d08ac9d5b137c8867e')

cryptocompare.get_price('BTC')

