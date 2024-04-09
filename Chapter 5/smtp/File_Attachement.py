import smtplib
import getpass 

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.header import Header

mail_host = "smtp-mail.outlook.com"
port = 587

sender = ''
receiver = ''
password = ''

message = MIMEMultipart()
message['From'] = Header(sender)
message['To'] = Header(receiver)
message['Subject'] = Header('Python SMTP')
message.attach(MIMEText('Python SMTP', 'plain'))
file1 = MIMEText(open('Picture 6A.jpg', 'rb').read(), 'base64')
file1["Content-Type"] = 'application/octet-stream'
file1["Content-Disposition"] = 'attachment; filename="file1.txt"'
message.attach(file1)
file2 = MIMEText(open('Picture 9A.jpg', 'rb').read(), 'base64')
file2["Content-Type"] = 'application/octet-stream'
file2["Content-Disposition"] = 'attachment; filename="file2.txt"'
message.attach(file2)

smtp = smtplib.SMTP(mail_host, port)
status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS Connection : {status_code} {response}")

status_code, response = smtp.login(sender, password)
print(f"[*] Logging in : {status_code} {response}")

smtp.sendmail(sender, receiver, message.as_string())
smtp.quit()
