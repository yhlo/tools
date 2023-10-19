# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:40:34 2023

@author: P170
"""

height=input("請輸入身高，單位為公分：")
weight=input("請輸入體重，單位為公斤：")

height_m=float(height)/100
height_m2=height_m*height_m
bmi=float(weight)/height_m2

if bmi < 18.5:
    print("您的bmi為 "+"%0.1f" %bmi,"您的體重過輕")    
elif bmi < 25 and bmi > 18.5:
    print("您的bmi為 "+"%0.1f" %bmi,"您的體重正常")
elif bmi < 30 and bmi > 25:
    print("您的bmi為 "+"%0.1f" %bmi,"您的體重過重")
elif bmi > 18.5:
    print("您的bmi為 "+"%0.1f" %bmi,"您的體重肥胖")
    
