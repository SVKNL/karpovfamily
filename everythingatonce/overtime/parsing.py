import imaplib
import email
from email.header import decode_header
import base64
from bs4 import BeautifulSoup
import re
mail_pass = "t4SPrvNZJEvRjwa1YxEc"
username = "karpovv1994@bk.ru"
imap_server = "imap.mail.ru"
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, mail_pass)
imap.select("INBOX")
r=imap.uid('search', "ALL")
print(r)
res, msg = imap.fetch(b'4', '(RFC822)')

msg = email.message_from_bytes(msg[0][1])


letter_from = msg["Return-path"]


letter_subject=decode_header(msg['Subject'])[0][0].decode()

payload=msg.get_payload()
for part in payload:
    print(part.get_content_type())  


print(letter_subject)