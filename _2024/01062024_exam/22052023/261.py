#f=open("27989_A.txt")
f=open("27989_B.txt")
n=int(f.readline())
a=[int(x) for x in f]
cnt=0
# for j in range(len(a)-1):
#     for i in range(j+1,len(a)):
#         if a[i]*a[j]%26==0:
#             cnt+=1
# print(cnt)

a2=[]
a13=[]
a26=[]
a0=[]
for x in a:
    if x%26==0:
        a26.append(x)
    elif x%13==0:
        a13.append(x)
    elif x % 2 == 0:
        a2.append(x)
    else:
        a0.append(x)

print (a26,a13,a2,a0)

suma=len(a26)*(len(a13)+len(a2)+len(a0)) +len(a2)*len(a13)+len(a26)*(len(a26)-1)/2
print(suma)
