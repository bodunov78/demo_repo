def fu1(a=1,b=2,c=""):
    print (a,b,c)

def fu2(st,en,sp):
    i=st
    a=[]
    x=st
    while x<en:

        a.append(x)
        x+=sp
    return iter(a)

def fu3(**parma):
    print (parma.keys(),parma.values())


#fu1(10,20,"sdfghjk")
fu3(abc=123,bcd=234,cde=345)

# for x in fu2(1,2,0.4):
#     print (x)

