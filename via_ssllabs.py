import requests
from datetime import datetime
import email_notification

def main():
    exp_dates = []
    hostname = 'www.mwam.com'
    response = requests.get(f"https://api.ssllabs.com/api/v3/analyze?host={hostname}&fromCache=on&all=done")
    raw_certs = response.json()


    for i in raw_certs['certs']:
        exp_dates.append(datetime.fromtimestamp(i['notAfter']/1000))
        
    certExpires = min(exp_dates)
    print(certExpires.strftime('%b %d %H:%M:%S %Y %Z')) # find the earliest expiration date in the certificate chain
    print((certExpires - datetime.now()).days,  " days before expiration")
    email_notification.send_notification((certExpires - datetime.now()).days)


if __name__ == "__main__":
    main()