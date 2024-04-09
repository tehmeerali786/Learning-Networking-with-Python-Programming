import poplib
import argparse 

def main(hostname, port, user, password):
    
    mailbox = poplib.POP3_SSL(hostname, port)
    
    try:
        mailbox.user(user)
        mailbox.pass_(password)
        response, listings, octate_count = mailbox.list()
        print(f"Here is response:  {response}")
        print(f"Here is response:  {octate_count}")
        for listing in listings:
            number, size = listing.decode('ascii').split()
            print("Message %s has %s bytes" % (number, size))
            
    except poplib.error_proto as exception:
        print("Login failed:", exception)
        
    finally:
        mailbox.quit()
        
        
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mailbox basic params")
    parser.add_argument('--hostname', action="store", dest="hostname")
    parser.add_argument('--port', action="store", dest="995")
    parser.add_argument('--user', action="store", dest="pythonparyani@gmail.com")
    
    given_args = parser.parse_args()
    hostname = given_args.hostname
    port = given_args.port
    user = given_args.user
    
    import getpass 
    password = getpass.getpass(prompt='Enter your password')
    
    main(hostname, port, user, password)
    
    
        