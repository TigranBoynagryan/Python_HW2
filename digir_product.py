# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 13:55:41 2021

@author: Tigran Boynagryan
"""

n = int(input())

digit_prod = 1

while n>0:
    last_dig = n%10
    
    if last_dig != 0:
        digit_prod *= last_dig
        
    n = (n-last_dig)//10

print(digit_prod)