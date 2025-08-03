import smtplib
from email.message import EmailMessage
inst = '''What is a Gmail App Password?
A Gmail App Password is a 16-character one-time password that Google generates for you to use in apps or programs (like your Python script) instead of your actual Gmail password.

You cannot use your normal Gmail password with smtplib. Google will block it.

Why You Need It
Gmail blocks “less secure apps” from logging in with normal passwords.

App Passwords bypass 2-Step Verification securely.

You use it only in code — not shared publicly.

️ How to Create an App Password (Step-by-Step)
 You must first enable 2-Step Verification on your Google Account.

 Steps:
Go to https://myaccount.google.com

Click on Security

Under “Signing in to Google”, enable 2-Step Verification (if not already enabled)

After enabling, go back and you'll now see App passwords

Click App passwords

Select:

App: Mail

Device: Other → type something like “Python CLI”

Click Generate

Copy the 16-character password (e.g., abcd efgh ijkl mnop) — no spaces when using it in code'''


def send_email():

    print("---Email Automation---")
    print("***Make sure internet is connected***")
    sender_email = input("Your Gmail Address:")
    print(inst)
    app_password = input("Enter app password:")
    receiver_email = input("Recipient Email:")
    subject = input("Subject:")
    body = input("Message : ")

    try:
        msg = EmailMessage()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.set_content(body)

        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls() 
        server.login(sender_email,app_password)
        server.send_message(msg)
        server.quit()

        print("✅Email sent successfully")

    except Exception as e:
        print("❌Failed to send email")
        print("Error:",e)

