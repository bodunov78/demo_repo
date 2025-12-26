from itertools import *


def flatten(container):
    for i in container:
        # if isinstance(i, (list, tuple)):

        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i


# flattened_list = list(flatten(list_of_lists))
def fu(s, e, c):
    # print (e)
    if len(s) == 0:
        # print(e)
        return tuple(e)
    else:
        # print(e)
        s1 = s[::]
        m = []
        for x in s:
            s1 = s[::]
            e1 = e[::]
            e1.append(x)
            c += 1
            s1.remove(x)
            # print(s1,e1)
            # print (e1,s1,c)
            m.append((s1, e1, c))

        # print(m)
        return [fu(*x) for x in m]


s = list('12345')
e = []
c = 0
# print (s)
m = fu(s, e, c)

a = []
# a=chain(*m)
# print (list(a))
# a = list(chain.from_iterable(m))
# print (a)
# flattened_list = list(flatten(m))
# print (flattened_list)
# print(list(map(''.join, m))
#
# while True

# a=[1,2,3]
# b=(1,2,3)
# c=[(1,12),(2,3)]

flag=0
while flag !=1:
    if isinstance(m[0],tuple):
        flag=1
        break
    for x in m:
        if isinstance(x,list):
            print (x,type(c))
            a = list(chain.from_iterable(m))
            m=a[:]
            break

print (m)