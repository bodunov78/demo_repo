#Найдите все натуральные числа, не превышающие 1010, которые соответствуют маске 1?3948*5 и при этом без остатка делятся на 3013.

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
