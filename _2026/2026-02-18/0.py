
#9804
def fufu(x,A):
    return (((x&29)!=0) <=(((x&17)==0) <=((x&A)!=0 )))

#13745
def fifi(x,y,A):
    return ((x<=9)<=((x*x)<=A))and (((y*y)<=A) <=(y<=9))

for A in range(0,100):
   m=[ fufu(x,A) for x in range(0,100)]
   if all(m)==True:
       print (A)

for A in range(-100,1000):
    m=[fifi(x,y,A) for x in range(200) for y in range(200)]
    if all(m) == True:
        print(A)


for a1 in range(-100,100):
    for a2 in range(a1+1,100):
        

# print (bin(100),oct(100),hex(100),f"{100:x}")