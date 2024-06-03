# 10000 77777
# Определите количество пятизначных чисел, записанных в восьмеричной системе счисления,
# в записи которых только одна цифра 6, при этом никакая нечётная цифра не стоит рядом с цифрой 6.



from fnmatch import *
cnt=0
for i in range(8**4,8**5):
    s=str(oct(i)[2:])
    ss=s
    s=s.replace('0','2').replace('4','2').replace('3','1').replace('5','1').replace('7','1')
    if s.count('6')==1:
        if s[-1]=='6' and s[-2]=='2':
            cnt+=1
            print (ss)
        elif s[0]=='6' and s[1]=='2':
            cnt += 1
            (print(ss))
        elif '262' in s:
            cnt += 1
            (print(ss))


print (cnt)