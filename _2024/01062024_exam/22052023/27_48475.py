f = open("27B_48475.txt")
n = int(f.readline())
a=[int(x) for x in f ]
b=[[0]*13,[0]*13,[0]*13]




cnt=0
suma=0
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if (a[i]+a[j])%3==0 and a[i]*a[j]%4096==0:
#             cnt+=1
#
#
#
# print(n,len(a),cnt)



for x in a:
    for j in range(12,-1,-1):
        if x%(2**j)==0:
            b[x%3][j]+=1
            break

print (b[0])


for i in range(13):
    for j in range(13):
        if i+j>=12:
            suma+=b[1][i]*b[2][j]
            #print(i,j,i+j)




for i in range(13):
    for j in range(i+1,13):
        if i+j>=12  and i!=j :
            suma=suma+b[0][i]*b[0][j]

for i in range(13):
        if 2*i>=12:
            suma=suma+b[0][i]*(b[0][i]-1)/2



#
# for k in range(12):
#     suma=suma+ b[0][k]*b[0][12-k]
# suma=suma+b[0][6]*(b[0][6]-1)
# #
# for k in range(13):
#      suma=suma+ b[1][k]*b[2][12-k]
#
#
#
#
print(suma)
print (b[2])
print (b[1])
