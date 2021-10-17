# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 21:54:16 2021

@author: Tigran Boynagryan
"""

N = int(input())
x= True

def sum_calc(N):
    dig_sum =0
    while N>0:
        last_dig = N%10
        dig_sum += last_dig
        N //=10
    return dig_sum

while x:
    print(N)
    N=sum_calc(N)
    if N//10 == 0:
        print(N)
        x = False