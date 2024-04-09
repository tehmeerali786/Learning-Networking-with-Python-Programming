import sys, smtplib, socket 

# this invokes the secure SMTP protocol (port 465, uses SSL)
from smtplib import SMTP_SSL, SMTP 
from email.mime.text import MIMEText 

try:
    msg = MIMEText("Test message", "plain")
    msg['Subject'] = "Sent from Python Programming"
    msg['From'] = ''
    
    #smtp = SMTP()
    #smtp.connect("smtp.gmail.com", 587)
    
    # create smtp session
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    # debug active
    smtp.set_debuglevel(True)
    # identify ourselves to smtp gmail client 
    smtp.ehlo()
    
    # if we can encrypt this session, do it
    if smtp.has_extn('STARTTLS'):
        # secure our email with tls encryption
        smtp.starttls()
        # re-identify ourselves as an encrypted connection
        smtp.ehlo()
        
    try:
        smtp.login("", "")
    except smtplib.SMTPException as e:
        print("Authentication failed", e)
        sys.exit(1)
        
        
    try:
        smtp.sendmail('', [''], msg.as_string())
    except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as e:
        print(" *** Your message may not have been sent!")
        print(e)
        sys.exit(1)
        
    finally:
        smtp.quit()
        
        
except(socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as e:
    print(" *** Your message may not have been sent!")
    print(e)
    sys.exit(1)
        
        
        