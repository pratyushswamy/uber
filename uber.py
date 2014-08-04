# ######################
# Submission for Uber  #
# By - Pratyush Swamy  #
# #######################

__author__ = 'nazareth'

import smtplib
from email.mime.text import MIMEText

# Mail Gun Credentials
user_mailgun = 'ubertest@sandbox1728e9728dbe444897dbaf89cd1c6d4f.mailgun.org'
pass_mailgun = 'ubertest8/14'

# Mandrill Credentials
user_mandrill = 'pratyush.swamy@hotmail.com'
pass_mandrill = 'X7Cuqt9FtA-YoqS2uH_y8A'

# Using MIME
def mime_msg(sub, body):
    email = MIMEText(body, 'plain')
    email['Subject'] = sub
    email['From'] = "Pratyush Swamy <pratyush@swamy.com>"
    return email


# SMTP connection for Mailgun
def mailgun(email, sendTo):  # 'sendTo' contains the list of emails for both mailgun() and mandrill()
    try:
        s = smtplib.SMTP('smtp.mailgun.org', 587)
        # s.set_debuglevel(True)
        s.login(user_mailgun, pass_mailgun)
        # using sendTo in 'to' will send emails to all the address in the list
        s.sendmail(email['From'], sendTo, email.as_string())
        s.quit()
        return True

    except smtplib.SMTPException as e:
        print(e)
        return False


# SMTP connection for Mandrill
def mandrill(email, sendTo):
    try:
        s = smtplib.SMTP('smtp.mandrillapp.com', 587)
        # s.set_debuglevel(True)
        s.login(user_mandrill, pass_mandrill)
        s.sendmail(email['From'], sendTo, email.as_string())
        s.quit()
        return True

    except smtplib.SMTPException as e:
        print(e)
        return False


if __name__ == '__main__':
    """
    Main function which controls the email service
    and chooses alternative email service if the first one fails.
    """
    print("Enter the required information below!!! ")
    to = str(input("Recipient (Use ',' for multiple emails):\n"))
    to = to.split(',')
    to = [x.strip(' ') for x in to]
    for i, x in enumerate(to):
        if "@" not in x:
            print("This is incorrect: " + x + "!!!!")
            to[i] = input("Please enter a valid email ID: ")

    subject = input("Subject of Email: ")
    message = input("Type the message: ")
    print("Sending Email through Mandrill!!")

    if mandrill(mime_msg(subject, message), to):
        print("Mail Sent Successfully!!!")
    else:
        """Call other mail service"""
        print("Mandrill failed... \n"
              "Calling Railgun!!!!")
        if mailgun(mime_msg(subject, message), to):
            print("Railgun Worked.... Mail Sent")
        else:
            print("Both Services are Down!!!")
            print("Try Later!!! \nGood Bye!!!!")