#Найдите все натуральные числа, не превышающие 1010, которые соответствуют маске 1?3948*5 и при этом без остатка делятся на 3013.



for i in range(0,10**10,3013):
    s=str(i)
    if s[0]=='1' and s[2:6]=='3948' and s[-1]=='5':
        print(i)







# a=[str(i).zfill(j) for i in range(1000) for j in range(4)]
# a.append('')
# print (a)


a=[str(i).zfill(j) for i in range(1000) for j in range(4)]

a.append('')
a=list(set(a))
a.sort()
print (a)
for i in range(10):
    for j in a:
        s=f"1{i}3948{j}5"
        n=int(s)
        if n%3013==0:
            print (n)
