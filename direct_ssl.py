import ssl
import socket
from datetime import datetime
# import email_notification

def main():
    hostname = 'www.mwam.com'
    port = '443'
    context = ssl.create_default_context()

    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname = hostname) as ssock:
            certificate = ssock.getpeercert()


    print(certificate['notAfter'])
    certExpires = datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')
    print((certExpires - datetime.now()).days,  " days before expiration")

    # email_notification.send_notification((certExpires - datetime.now()).days)

if __name__ == "__main__":
    main()