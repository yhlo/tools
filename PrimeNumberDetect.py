# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 16:27:47 2023

@author: P170
"""

prime_number=int(input("請輸入一個數字"))

pn_squa=int(prime_number ** 0.5)
pn_squa_rou=round(pn_squa)
#print(pn_squa_rou)

pn_list={}
for i in range(pn_squa_rou):
  pn_list[i]=0
#print(pn_list)

for j in range(1,pn_squa_rou):
  if prime_number % j == 0:
      pn_list[j] = 1
#print(pn_list)

k=0
cont=0
while k < pn_squa_rou:
  if pn_list[k] == 1:
    cont += 1
  k +=1

if cont > 1 and pn_list[1] == 1:
  print(prime_number,"不是質數")
else:
  print(prime_number,"是質數")