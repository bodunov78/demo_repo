from random import *
print(randint(5,10))


arr=[randint(1,100) for x in range(10)]
print (arr)

# arr=[2,3,5,4,66,77,88,56,65,33,33333,0,-10]

d={"d2":0,"d3":0,'d5':0,'d0':0}
print (d)
for a in arr:
    if a%2==0:
        d['d2']+=1


    if a % 3 == 0:
        d['d3'] += 1

    if a % 5 == 0:
        d['d5'] += 1

    if (a%2 and a%3 and a%5):
        d['d0']+=1

print (d)