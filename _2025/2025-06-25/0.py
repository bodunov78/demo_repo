from itertools import *
from string import ascii_lowercase
gen=("".join(x) for x in product(ascii_lowercase,repeat=2))
for x in range(50):
    print (next(gen),end=" ")

cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]

gen=(cities[i%6] for i in range(1_000_000))
for i in range(20):
    print(next(gen), end=" ")


a=0
b=10
def frange(a,b,s):
    m=[]
    while a<b+s:
        m.append(a)
        a=a+s
    return(m)


gen=( round((0.5 * pow(x, 2) - 2.0),2) for x in frange(a,b+0.01,0.01))
for x in range(20):
    print (next(gen),end=" ")

