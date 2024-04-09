import smtplib
import getpass 

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.header import Header

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = 'ali786467@hotmail.com'
TO_EMAIL = 'freelanceali786@gmail.com'
PASSWORD = getpass.getpass("Enter password: ")

message = MIMEMultipart('Python SMTP HTML Version', 'plain')
message['Subject'] = Header('Python Programming!')
message['From'] = Header(FROM_EMAIL)
message['To'] = Header(TO_EMAIL)

html = ""
with open("mail.html", "r") as file:
    html = file.read()
    
html_part = MIMEText(html, 'html')
message.attach(html_part)

smtp = smtplib.SMTP(HOST, PORT)
status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS Connection : {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in : {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())
smtp.quit()
