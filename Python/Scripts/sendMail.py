import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_content = '''Hello,
This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
Thank You
'''

class EmailSender():
  
  def __init__(self):
    self.__sender_address = 'oscarkaka222@gmail.com'
    self.__sender_pass = 'dyqwducdroumngxo'
    self.__receiver_address = 'oscarkaka222@gmail.com'
    
  def __load_email_content(self):
    message = MIMEMultipart()
    message['From'] = self.__sender_address
    message['To'] = self.__receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'  
    message.attach(MIMEText(mail_content, 'plain'))
    return message.as_string()

  def send(self):
    session = smtplib.SMTP('smtp.gmail.com', 587) 
    session.starttls()
    session.login(self.__sender_address, self.__sender_pass)
    text = self.__load_email_content()
    session.sendmail(self.__sender_address, self.__receiver_address, text)
    session.quit()

email_sender = EmailSender()
email_sender.send()