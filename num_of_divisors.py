# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 21:24:24 2021

@author: Tigran Boynagryan
"""


 
# function to count the divisors
def countDivisors(n) :
    cnt = 0
    for i in range(1, n//2+1) :
        if n%i ==0:
            cnt = cnt + 1
              
    return cnt+1
     

 
print(countDivisors(144))