import getpass
import smtplib 
from email.mime.text import MIMEText 
from email.header import Header 

sender = 'ali786467@hotmail.com'
receiver = 'freelanceali786@gmail.com'

mail_host = 'smtp-mail.outlook.com'
user = 'ali786467@hotmail.com'
password = getpass.getpass("Enter password: ")

mail_message = """
<p>Python Programming</p>
<p><a href="http://www.python.org">python software link</a></p>

"""

message = MIMEText(mail_message, 'html')
message['From'] = Header(sender)
message['To'] = Header(receiver)

subject = 'Python SMTP'
message['subject'] = Header(subject)


smtp = smtplib.SMTP(mail_host, 587)

try:
    smtp.connect(mail_host, 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(user, password)
    smtp.sendmail(sender,receiver, message.as_string())
except smtplib.SMTPException as exception:
    print(exception)
finally:
    smtp.quit()
    