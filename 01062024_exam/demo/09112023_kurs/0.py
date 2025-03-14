arr=[2,3,5,4,66,77,88,56,65,33,33333,0,-10]

d={"chet":0,"nechet":0}
print (d)
for a in arr:
    if a%2==0:
        print ("chet",a)
        d['chet']+=1
    else:
        print ("nechet",a)
        d['nechet'] += 1
print (d)
