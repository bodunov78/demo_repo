from time import *
def f1():
    ts=time()
    with open("81808.txt") as f:
        s=f.readline()
        m=0
        am=[]
        for l in range(len(s)):
            for r in range(l+m,len(s)):
                ss=s[l:r+1]
                if  ss.count('2025')>=90 and ss.count('Y')==80:
                        am.append((len(ss),ss))
                        m = max(m, len(ss))
                elif ss.count('Y')>80:
                    break

        print (m)


        print (len(max(am)),max(am))

    print (time()-ts)
def f2():
    ts = time()
    with open("81808.txt") as f:
        s = f.readline()
        m = 0
        am = []
        for l in range(len(s)):
            for r in range(l + m, len(s)):
                ss = s[l:r + 1]
                if ss.count('Y') == 80 and ss.count('2025') >= 90:
                    am.append((len(ss), ss))
                    m = max(m, len(ss))
                elif ss.count('Y') > 80:
                    break

        print(m)

        print(len(max(am)), max(am))

    print(time() - ts)

f1()