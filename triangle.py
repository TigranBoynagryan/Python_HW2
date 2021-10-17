# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 14:02:20 2021

@author: Tigran Boynagryan
"""

a=int(input())
b=int(input())
c=int(input())


if a+b>c and a+c>b and b+c>a: 
    if a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
        print("Obtuse Triangle")
    elif a**2 + b**2 > c**2 or a** 2 + c**2 > b**2 or b**2 + c**2 > a**2:
        print("Acute Triangle")
    elif a**2 + b**2== c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Right Triangle")
else:
    print("No Triangle")


