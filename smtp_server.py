import smtplib, smtpd
import asyncore
import email.utils
from email.mime.text import MIMEText
import threading
from snowmail.encrypt import Crypter

#key = 
class SMTPReceiver(smtpd.SMTPServer):

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

        # print data

        # def send_response():
        #     msg = MIMEText('Hello world!')
        #     msg['To'] = email.utils.formataddr(('Recipient', mailfrom))
        #     msg['From'] = email.utils.formataddr(('Author', 'name@example.org'))
        #     msg['Subject'] = ''

        #     print 'Connecting to mail server'
        #     server = smtplib.SMTP()
        #     server.set_debuglevel(1)
        #     server.connect()
        #     print 'Attempting to send message'
        #     try:
        #         server.sendmail('name@example.org', [mailfrom], msg.as_strtring())
        #     except Exception, ex:
        #         print 'Could not send mail', ex
        #     finally:
        #         server.quit()
        #     print 'Finished sending message'
        # threading.Thread(target=send_response).start()
        # return

def main():
    server = SMTPReceiver(('', 25), None)
    asyncore.loop()

if __name__ == '__main__':
    main()