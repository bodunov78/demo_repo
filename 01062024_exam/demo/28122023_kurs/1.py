# Тип 17 37341


ar19=[[] for i in range(19)]
ost19=[0]*19


chet19=[]
nechet19=[]
chet=[]
nechet=[]

print (ar19)
with open("17.txt") as f:
    for x in f:
        ar19[int(x)%19].append(int(x))
        if int(x)%19==0:
            if int(x)%2==0:
                chet19.append(int(x))
                if len(chet19)>2:
                    chet19.sort()
                    chet19=chet19[1:]
            else:
                nechet19.append(int(x))
                if len(nechet19)>2:
                    nechet19.sort()
                    nechet19=nechet19[1:]
        else:
            if int(x)%2==0:
                chet.append(int(x))
                if len(chet)>2:
                    chet.sort()
                    chet=chet[1:]
            else:
                nechet.append(int(x))
                if len(nechet)>2:
                    nechet.sort()
                    nechet=nechet[1:]
# chet.sort()
# nechet.sort()
# chet19.sort()
# nechet19.sort()

print(chet,nechet,chet19,nechet19)

a=len(chet19)*(len(chet19)-1)/2
a+=len(nechet19)*(len(nechet19)-1)/2

a+=len(chet19)*len(chet)
a+=len(nechet19)*len(nechet)
print(a)
maxi=max(chet19[-1]+chet19[-2],chet19[-1]+chet[-1],nechet19[-1]+nechet19[-2],nechet19[-1]+nechet[-1])
print (maxi)