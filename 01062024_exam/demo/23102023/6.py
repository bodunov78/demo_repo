a=[1,2,3,4,5,6,7,1,1]
if len(a) == len(set(a)):
    print ("Уникальные")
else:
    print("Не уникальные")
print(a.count(1))

print(a,list(set(a)))
b=list(set(a))
b.sort(reverse=1)
print(b)
