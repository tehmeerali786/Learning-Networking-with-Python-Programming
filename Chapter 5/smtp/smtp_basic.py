import smtplib 

smtp = smtplib.SMTP('smtp.gmail.com', 587)

try:
    smtp.sendmail('sender', ['reciever'], 'This is a test message.')
except SMTPSenderRefused as exception:
        print("Error: unable to send email: " + exception)
finally:
    smtp.quit()