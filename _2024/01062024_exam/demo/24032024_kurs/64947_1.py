#64947

a = [int(s) for s in open('64947.txt')]
a832 = max([x for x in a if x % 1000 == 832])
count = 0
s3 = []
for i in range (len(a) - 2):
    troika = [a[i] , a[i+1] , a[i+2]]
    print (troika)
    a3 = [x for x in troika if x % 3 == 0]
    a5 = [x for x in troika if x % 5 == 0]
    raz4 = [x for x in troika if len(str(x)) == 4]
    if sum(troika) > a832:
        if len(a3) < len (a5):
            if 0 < len(raz4) < 3:
                s3.append(sum(troika))
print(s3)
print(len(s3),max(s3))