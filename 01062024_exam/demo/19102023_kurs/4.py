arr=[]
for i in range(100,200):
    s='1'*i
    while '111' in s:
        s=s.replace('111','22',1)
        s=s.replace('222','11',1)
    arr.append(s.count('1'))

print (arr)

