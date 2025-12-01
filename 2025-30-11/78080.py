from re import *

def f1():
    with open("24_78080.txt") as f:
        s=f.readline()

        d=set(['**','--','*-','-*'])
        print (d)
        di=set("01234567-*")
        ds=set(s)
        dsl=ds-di
        dsl.update(d)
        print (dsl)
        for c in dsl:
            s=s.replace(c,':')
        print(s[:100])
        a=s.split(':')
        n=[]
        for x in a:
            s=x.lstrip('-*').rstrip("-*")
            n.append((len(s),s))
        print (max(n))






def f2():
    text = open('24_78080.txt').readline()
    s = findall(r'(?=((?:0|[1-7][0-7]*)(?:\*(?:0|[1-7][0-7]*))*(?:-(?:0|[1-7][0-7]*))*))', text)

    print(len(max(s, key=len)))
    a=[(len(x),x) for x in s]
    print (max(a))

f1()
f2()