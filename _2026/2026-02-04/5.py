
a=[1,2,3,4,5,6,9]
# не делится на 3
d=[int(not(not(x%3))) for x in a]

# делится на 3
d=[int(not(x%3)) for x in a]

print (d)