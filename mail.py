import smtplib
import getpass
import requests
from bs4 import BeautifulSoup

gmail_user = input("Enter your gmail account: ")
gmail_password = getpass.getpass("Enter your password: ")

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    print("Connected to gmail servers")
except:  
    print("Something went wrong...")

from_mail = gmail_user
to = input("Who should receive the mail?")
body = "Buenas tardes\n, a continuación encontrará el informe que prometí en mandarle. \nUn saludo."

# Send the mail to SMTP gmail server
server.sendmail(from_mail, to, body)

server.close()