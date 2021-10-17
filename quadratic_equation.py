# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 19:54:00 2021

@author: Tigran Boynagryan
"""

a=float(input())
b=float(input())
c=float(input())
D=b**2-4*a*c


def quad_solve(a,b,c,D):
    x1 = (-b+D**(1/2))/2*a
    x2 = (-b-D**(1/2))/2*a
    if D == 0:
        return f"One solution: {x1}"
    elif D>0:
        return f"Two solution: {x1} {x2}"
    else:
        return "No solutions"
        
        
def non_quad(a,b,c):
    if a==0 and b==0 and c==0:
        return "infinite Solutions"
    elif b ==0:
        return "No Solutions"
    else:
        return f"One solution: {-c/b}"

if a>=1:
    print('Quadratic Equation')
    print(f'Discriminant: {D}')
    print(quad_solve(a,b,c,D))
    
else:
    print('Non-quadratic Equation')
    print(non_quad(a,b,c))
    



int(n**(1/2)) + 1