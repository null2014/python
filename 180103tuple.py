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


def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)


person('Michael',30)

person('Bob',35,city='BJ')

