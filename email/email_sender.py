import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Boni Legalzinho'
email['to'] = 'italovianelli@gmail.com'
email['subject'] = 'Email teste'

email.set_content(html.substitute(name='Italous'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('testeitalov@gmail.com', 'Marketing2017')
    smtp.send_message(email)
    print('all good boss')
