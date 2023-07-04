import smtplib
import getpass

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587) #try 465 if any errors

smtp_obj.ehlo()

smtp_obj.starttls()

email = input("Email Id please:")
password = getpass.getpass('Password please:')

smtp_obj.login(email,password)

from_address = email
to_address = input("enter the email to be sent to: ")
subject = input("enter the subject of email:")
body = input("enter the body of email:")
msg = "Subject: " + subject + "\n" + body

response = smtp_obj.sendmail(from_address, to_address, msg)

if response == {}:
    print("Email sent successfully!")
else:
    print("Error in sending email")

smtp_obj.quit()
