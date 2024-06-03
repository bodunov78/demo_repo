arr=[]
for i in range(100,1000,5):
    # print (i)
    s=str(i)
    ch1=int(s[0])+int(s[1])
    ch2 = int(s[1]) + int(s[2])
    # print(max(ch1,ch2)*(10**len(str((min(ch1,ch2)))))+min(ch1,ch2))
    ch3=int(str(max(ch1,ch2))+str(min(ch1,ch2)))
    if ch3==1412:
        arr.append(i)
        print (i,ch3)
print (len(arr),max(arr),min(arr))
    # print (type(s),type(i),s,":",int(s[0])+int(s[1]),int(s[1])+int(s[2]))