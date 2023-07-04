import imaplib
import getpass
import email

M = imaplib.IMAP4_SSL("imap.gmail.com")
print(""" ************* Welcome to email Garbage Collector ************* 
        Before you access this tool please follow the steps below and generate your app password:
        1. Go to https://myaccount.google.com/security and login using your email id
        2. Turn on two step verification  by clicking on it and following the steps.
        3. Once step 2 is done, visit link in step1
        4. Click on app password which is just below two step verification
        5. login using the email and select device as 'others' and enter 'python scipt' as app and click ok
        6. Now in you will be shown a passcode in the yellow background save that 16 digit alphanumeric password somewhere safe.p
        7. Use this password to login to your email account while using this script.
""")
user_email = input("enter you gmail email id: ")
user_password = getpass.getpass("enter your gmail application password: ")

response_type, response = M.login(user_email, user_password)
if(response_type == "OK"):
    print("login successful!")
else:
    print("login failure!")
    exit()

#print(M.list())
folder_name = input("enter one of the above folders in lowercase to delete the mails from(for eg: inbox, sent): ")

M.select(folder_name)

user_email_set = input("enter email lists seperated by ',' to be deleted: ")

email_list_to_delete = user_email_set.split(',')
for item in email_list_to_delete:
    typ, data = M.search(None, 'FROM ' + item)
    mail_list = data[0].decode("utf-8").split(" ")
    for email_id in mail_list:
        M.store(email_id, '+FLAGS', '\\Deleted')

deleted_list = M.expunge()
print(str(len(deleted_list[1])) + " emails are deleted")

