# 1:01
def f(s):
    while '12' in s or '322' in s or '222' in s:
        if '12' in s:
            s=s.replace('12','2',1)

        if '322' in s:
            s = s.replace('322', '21', 1)

        if '222' in s:
            s = s.replace('222', '3', 1)

        d=[int(x) for x in s]

    return sum(d)
#1:06



for n in range(3,10**4+1):
    s="1"+'2'*n
    if f(s)==15:
        print(n)
        break