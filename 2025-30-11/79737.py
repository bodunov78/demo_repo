from string import *
from time import *

# print (printable)
def f1():
    ts=time()
    sl=set("0123456789ABCD")

    with open("79737.txt") as f:

        s=f.readline()
        print(len(s))
        sd=set(s)
        print (sd-sl)
        sdl=sd-sl
        print (sdl)

        for c in sdl:
            s=s.replace(c,':')



        k=[]
        a=s.split(':')
        print (len(a))
        # m=[x.lstrip('0') for x in a if len(x.lstrip('0'))>0]
        #
        m=[(len(x),x) for x in a]
        for x in a:
            ss=x.lstrip('0').rstrip('13579BD')
            k.append((len(ss),ss))
        # print (max(k))

        # v="123457657"
        # # m=v.rstrip('75').lstrip('12')
        # print (m)
        # #
        #     k.append((int(ss),len(ss)))
        print (max(k))
        print (time()-ts)
def f2():
    ts=time()
    import re
    k=[]
    string = open('79737.txt').readline()
    pattern = r'[123456789ABCD][0123456789ABCD]*[02468AС]'
    iterator = re.finditer(pattern, string)
    abc=[i.group() for i in iterator]
    # print (abc)
    # otv = max([i.group() for i in iterator], key=len)
    # print(len(otv))
    for i in abc:
        k.append((len(i),i))
    print (max(k))
    print (time()-ts)
f2()