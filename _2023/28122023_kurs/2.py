# Тип 17 37341


ar19=[[] for i in range(19)]
print (ar19)
with open("17.txt") as f:
    arr=[int(i) for i in f]
maxpair=0
cnt=0
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        if (arr[i]-arr[j])%2==0 and (arr[i]*arr[j]%19==0):
            cnt+=1;
            maxpair=max(maxpair,arr[i]+arr[j])

print (cnt,maxpair)