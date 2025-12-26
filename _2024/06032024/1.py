a=[]
a=["A","B","C","D"]

a.append("Мама")
print (a[-1])
print (a)

a[-1]="Папа"
print (a)
a[0]="Мама"
print (a)

a=[9,8,7,6,5,4,3,2,1]

for x in a:
    print ("Это -",x)

for i in range(len(a)):
    print (i,a[i])

for i,v in enumerate(a):
    print (i,"---",v)
    if i==5:
        a[i]="Папа"

print (a)

a=[12,23,34,45,56,67,78,89,90,1]

print (a)

for i in range(len(a)):
    a[i]=a[i]+777

print (a)


# к каждому элементу массива прибавить 777
# распечатать массив до и после










