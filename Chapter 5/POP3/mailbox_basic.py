import poplib 

mailbox = poplib.POP3_SSL("pop.gmail.com", 995)
mailbox.user("")
mailbox.pass_("")

print(mailbox.getwelcome())

messages = len(mailbox.list()[1][:10])

print(mailbox.list()[1][:10])

print(messages)

for index in range(messages):
    for message in mailbox.retr(index+1)[1][:10]:
        print(message)
        
mailbox.quit()