# Certainly! To verify an email address using the SMTP protocol in Python, you can use the `smtplib` module, which is part of the standard library. The following example demonstrates a simple script that connects to the recipient's email server and attempts to verify the existence of an email address:


import smtplib

def verify_email(email_address):
    # Split the email address to extract the domain and username
    username, domain = email_address.split('@')

    # Set the email server for the recipient's domain
    email_server = f"mail.{domain}"

    try:
        # Connect to the recipient's email server
        with smtplib.SMTP(email_server) as server:
            # Try to verify the email address
            response_code, _ = server.verify(email_address)

            # Check the response code
            if response_code == 250:
                print(f"Email address '{email_address}' is valid.")
            else:
                print(f"Email address '{email_address}' is not valid.")
    except smtplib.SMTPConnectError:
        print(f"Could not connect to the email server for '{domain}'.")
    except smtplib.SMTPServerDisconnected:
        print(f"Disconnected from the email server for '{domain}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
email_to_verify = "someone@example.com"
verify_email(email_to_verify)


# Please note the following:

# - This script splits the email address into the username and domain parts and assumes a simple format. In a production environment, you might want to handle email parsing more robustly.

# - The script attempts to connect to the email server and use the `verify` method. Keep in mind that not all email servers support the `verify` method, and some may even disable it for security and privacy reasons.

# - It's essential to handle exceptions gracefully to account for various error scenarios, such as connection issues or unexpected errors.

# - This script is for educational purposes and might not be suitable for all scenarios. Email verification is a complex task, and there are specialized services and libraries that provide more comprehensive solutions.

# Before running the script, make sure to replace the example email address (`someone@example.com`) with the one you want to verify. Additionally, consider using this script responsibly and in accordance with the policies of the email servers you are interacting with.