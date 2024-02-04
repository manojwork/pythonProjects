import smtplib as sm
my_mail="manojbabu.mandhala@gmail.com"
recever="manojmass421@gmail.com"
password="bvydresbbflrglwb"
connect=sm.SMTP("smtp.gmail.com",port=587)
connect.starttls()
connect.login(user=my_mail,password=password)
connect.sendmail(from_addr=my_mail,to_addrs=recever,msg="subject:hello\n\n hello how are you ")
connect.close()