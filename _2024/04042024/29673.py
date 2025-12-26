# Найдите все натуральные числа, принадлежащие отрезку [123456789;223456789] и имеющие ровно три нетривиальных делителя
def didi(a):
    cnt=0
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            cnt+=1
        if cnt>3:
            break
    return cnt
m=[]
for i in range(123456789,223456789+1):

    if didi(i)==3:
        print(i)
        m.append(i)


