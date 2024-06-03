f = open("27A_47024.txt")
n = int(f.readline())
a=[int(x) for x in f]



b=[0]*1111

print(len(a),n)
for x in a:
    b[x%1111]+=1


for i in range(len(b)):
    cnt+=b[i]*b[1110-i]

print (b)