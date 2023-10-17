# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 11:19:36 2021

@author: P170
"""

print("input your birthday in 19XXXXXX type")
x = input()
print("your birthday is " + x)
x_int = int(x)


i = 1
plus = 0
y = [0,0,0,0,0,0,0,0]
for i in range(8):
    y[i] = int(x[i])
    plus = plus+y[i]
    
if plus > 9:
    td = int(plus/10)
    ud = plus - td*10
    number = td + ud
    
    if number > 9:
        nu1 = int(number/10)
        nu2 = number - nu1*10
        number1 = nu1 + nu2
#        print(number1)
        number = number1
else:
    number = plus

print("Lucky number is "+ str(number))

k = str('number1' in vars())

if k == 'False':
    print("Destiny Composite is "+str(td)+str(ud)+"/"+str(number))
else:
    print("Destiny Composite is "+str(td)+str(ud)+"/"+str(nu1)+str(nu2)+"/"+str(number))