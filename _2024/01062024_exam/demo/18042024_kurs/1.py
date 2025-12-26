import operator
a=[x for x in range(20,101)]


b=[0]*3+[1]*5+[0]*(80-8)
print (a)
print (b)
import operator
result = list(map(operator.add, a, b))
print (result)


