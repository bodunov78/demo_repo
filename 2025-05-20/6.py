from itertools import *
from fnmatch import *
from functools import *
from math import *
from pickle import *
from turtle import *


k=20
tracer(0)
screensize(5000,5000)
down()
for i in range(6):
    fd(19*k)
    rt(90)
    fd(21*k)
    rt(90)
up()
fd(5*k)
rt(90)
fd(4*k)
lt(90)
down()
for i in range(6):
    fd(54*k)
    rt(90)
    fd(78*k)
    rt(90)
up()

for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3,"red")


done()
