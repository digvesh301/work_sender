from multiprocessing import connection
import smtplib

# import datatime
# give day and hour

import datetime as dt
import smtplib
from struct import pack
my_email="pythonangel09@gmail.com"
password="I91Ej7)%WGw75Xo$Y%"






today=dt.datetime.now()
hour=today.hour
min=today.minute

def send_mail(x):
     
     with open(f"To_Do_list/{x}list.txt") as read_file:
         read_txt=read_file.read()
         print(read_txt)
    
     connection=smtplib.SMTP("smtp.gmail.com",587)
     connection.starttls()
     connection.login(user=my_email,password=password)
     connection.sendmail(from_addr=my_email,to_addrs="digveshpatel969@gmail.com",msg=f"subject:task\n{read_txt}")
     connection.close()


while True:
    if hour==6 and min==30:
        send_mail(1)
    if hour==8 and min==30:
        send_mail(2)
    if hour==15 and min==30:
        send_mail(3)
    if hour==17 and  min==50:
        send_mail(4)
    if hour==20 and min==55:
        send_mail(5)