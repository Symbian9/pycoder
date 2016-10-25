#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-07-13 16:35:33
# @Last Modified by:   anchen
# @Last Modified time: 2016-07-13 17:24:13


import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.163.com"
mail_user = "fz420"
mail_pass = "618="


sender = 'fz420@163.com'
receivers = ['fz420@qq.com']


message = MIMEText('hello qq this is 163mail test', 'plain', 'utf-8')
message['From'] = Header('fz420@163.com', 'utf-8')
message['To'] = Header("fz420@qq.com", 'utf-8')


subject = 'Python SMTP mail test '
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error:无法发送邮件")

