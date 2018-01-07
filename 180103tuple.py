# -*- coding: utf-8 -*-

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
