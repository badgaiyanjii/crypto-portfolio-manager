import random
import smtplib

def generate_otp():

    return str(random.randint(100000,999999))


def send_otp(email,otp):

    sender="your_email@gmail.com"
    password="your_app_password"

    server=smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()

    server.login(sender,password)

    message=f"Subject: Crypto Login OTP\n\nYour OTP is {otp}"

    server.sendmail(sender,email,message)

    server.quit()