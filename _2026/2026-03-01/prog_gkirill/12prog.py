x1,y1=map(int,input("1tochka: ").split())
x2,y2=map(int,input("2tochka: ").split())
d=((x2-x1)**2 +(y2-y1)**2)**(1/2)
print(d)

print()

def gip(x11,y11,x22,y22):
    return ((x22-x11)**2 +(y22-y11)**2)**(1/2)
g=gip(x1,y1,x2,y2)
print(g)