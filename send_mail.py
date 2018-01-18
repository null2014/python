# -*- coding: utf-8 -*-
#send email

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


sender = 'dane.liu@huolala.cn'
receivers = ['2289975022@qq.com']

# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="dane.liu@huolala.cn"    #用户名
mail_pass="HLLdane388"   #口令 
 
 
#發送有連結的郵件
'''
mail_msg = """
<p>hello morinig...</p>
<p><a href="https://www.baidu.com">這是個連結</a></p>
"""
message = MIMEText(mail_msg,'html','utf-8')
message['from'] = Header('just do it,study hard ,play hard')
message['to'] = Header('study hard')
subject = 'study hard'
message['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
'''

#發送附件的郵件
message = MIMEMultipart()
message['from'] = Header('just do it,study hard ,play hard')
message['to'] = Header('study hard')
subject = 'study hard'
message['Subject'] = Header(subject,'utf-8')

#郵件徵文內容
message.attach(MIMEText('this is a jobs'))

#附件1
att1 = MIMEText('text.txt','rb').read(),'base64'','utf-8')


