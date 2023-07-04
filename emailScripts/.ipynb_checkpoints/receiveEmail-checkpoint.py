import imaplib
import getpass

M = imaplib.IMAP4_SSL('imap.gmail.com')

email = input("enter your email id:")
password = getpass.getpass("enter password:")

M.login(email, password)

M.list()

M.select('inbox')

type, data = M.search(None, 'BEFORE 31-12-2016')

if typ == 'OK' && data != []:
    print("Successfully found!")
else:
    print("no emails found!")

email_id = data[0]
result, email_data = M.fetch(email_id, '(RFC822)')


