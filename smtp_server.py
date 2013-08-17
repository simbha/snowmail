import smtplib, smtpd
import asyncore
import email.utils
from email.mime.text import MIMEText
import threading
from snowmail.encrypt import Crypter


class SMTPReceiver(smtpd.SMTPServer):

    def __init__(self, secret_key):
        self.secret_key = secret_key

    def process_message(self, peer, mailfrom, rcpttos, data):
        print peer
        header = '\n'.join([
            'Receiving message from:{0}'.format(peer), 
            'Message addressed from:{0}'.format(mailfrom),
            'Message addressed to  :{0}'.format(rcpttos),
            'Message length        :{0}'.format(len(data))
        ])
        cr = Crypter('934a26c6ec10c1c44e1e140c6ffa25036166c0afd0efcfe638693e6a')
        encrypted_header = cr.encrypt(header)
        encrypted_data = cr.encrypt(data)
        with open('test.txt', 'a') as txt_file:
            txt_file.write(encrypted_header)
            txt_file.write(encrypted_data)


def main():
    server = SMTPReceiver(('', 25), None)
    asyncore.loop()

if __name__ == '__main__':
    main()