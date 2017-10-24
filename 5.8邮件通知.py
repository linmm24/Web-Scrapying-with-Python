import smtplib
from email.mime.text import MIMEText
from email.header import Header
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

#参数为主题和内容
def sendMail(subject, body):
    mail_host = "smtp.qq.com"
    mail_user = "937696414@qq.com"
    mail_pass = "zosxcihgcsvdbcie"  #qq邮箱在第三方登陆的授权码
    sender = '937696414@qq.com'
    receivers = ['937696414@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEText(body, 'plain', 'utf-8')
    message['From'] = Header("python", 'utf-8')  # 发件人
    message['To'] = Header("24号同学", 'utf-8')  # 收件人
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("失败")

bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"),"html.parser")
while(bsObj.find("a", {"id":"answer"}).attrs['title'] == "NO"):
    print("It is not Christmas yet.")
    time.sleep(3600)
    bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"),"html.parser")

subject= "It's Christmas!"


body = "According to http://itischristmas.com, it is Christmas!"
sendMail(subject,body)
