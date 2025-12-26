from adx import *
def f(n):
    if n==1 or n ==2 : return 3
    elif n==0 : return 0
    elif n>2 : return 5*f(n-1)-4*f(n-2)

print (f(15))




adsp(22)