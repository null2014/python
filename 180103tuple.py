# -*- coding: utf-8 -*-
import sys

print (sys.version)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
#print apple
print(L[0][0])

#print python
print(L[1][1])

#print lisa

print(L[2][2])


height = 1.75
weight = 80.5
BMI= weight/(height*height)



def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)


person('Michael',30)

person('Bob',35,city='BJ')


L = ['Bart', 'Lisa', 'Adam']

i = 0
n=len(L)

while i < n:
    print('hello,%s',L[i])
    i = i + 1



sum = 0
for x in range(101):
    sum = sum + x
print(sum)

n1 = 255
n2 = 1000
s = hex(n2)
print(s)



def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


#異動一個點倒另一個點，得出新點的座標
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny    

#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0的两个解

import math

def quadratic(a, b, c):
    pass
    
    

#why i can't do this
#def person(name, age, *args, city, job):
 #   print(name, age, args, city, job)


def add_end(L=[]):
    L.append('END')
    return L

s = add_end(['1','2'])
print s

s2 = add_end()
print s2

s2 = add_end()
print s2


#遞歸
def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num -1,num * product)

#漢諾塔異動的例子




#切片

F = ['Micheal','Sarah','Tray','Bob','Jack']

print ('F[0:3] = ',F[0:3])

print ('F[2:3] = ',F[2:3])
print ('F[-2:] = ',F[-2:])

#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
s = [' ' ,'this', 'is', 'a', 'book','']
def trim(s):
    s[1:-1]
    return s
print s


#迭代
d = {'a':1,'b':2,'c':3}

for key in d:
    print(key)


#send email

import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender = 'dane.liu@huolala.cn'
receivers = ['2289975022@qq.com']

# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="dane.liu@huolala.cn"    #用户名
mail_pass="HLLdane388"   #口令 
 
 

message = MIMEText('test email')
message['from'] = Header('just do it,study hard ,play hard')
message['to'] = Header('study hard')
subject = 'study hard'
message['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"