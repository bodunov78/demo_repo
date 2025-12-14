from itertools import *
from turtle import *
from time import *
from itertools import *
from math import *
from ipaddress import *
from math import *
from functools import *
from string import *
from pickle import *
def f1():


    # 2 25340

    t = "13,16,18,23,24,36,47,56,57,78"
    g = "HD,DA,AC,AG,CG,GE,EF,FH,CB,BH"
    t = t + ',' + t[::-1]
    g = g + ',' + g[::-1]

    s = "ABCDEFGH"

    for ss in permutations(s):
        nt = g
        for i, v in enumerate(ss):
            nt = nt.replace(v, str(i + 1))
        if set(nt.split(',')) == set(t.split(',')):
            print(ss)

# 25341
def f2():
    def f(x,y,z,w):
        return ( (w == z )or (not(y<=w)) or (not(x)) )

    for a1, a2, a3, a4,a5 in product([0, 1], repeat=5):
        tab = [(a1, 0, 1, 0), (a2, 1, 1, a3), (0, a4, a5, 0)]
        if len(tab) == len(set(tab)):
            for p in permutations('xyzw'):
                if [f(**dict(zip(p, r))) for r in tab] == [0, 0, 0]:
                    print(p)

def f4():
    def thre(n):
        s=""
        while n>0:
            ost=n%3
            n=n//3
            s=str(ost)+s
        return s

    def f(n):
        s=thre(n)
        if len(s)<2:
            return 10000

        if n%3==0:
            s=s+s[-2:]
        else:
            a=(int(s[-2])+int(s[-1]))*3
            s=s+thre(a)

        return int(s,3)

    m=[]
    for n in range(1,1000):
        k=f(n)
        if k>228:
            m.append(k)
    print (min(m))




def f6():


    screensize(5000, 5000)
    tracer(0)
    down()
    k = 20
    for i in range(6):
        fd(33 * k)
        rt(90)
        fd(20 * k)
        rt(90)
    up()

    fd(3 * k)
    rt(90)
    fd(9 * k)
    lt(90)
    down()

    for i in range(6):
        fd(24 * k)
        rt(90)
        fd(25 * k)
        rt(90)

    up()

    for i in range(-50, 50):
        for j in range(-50, 50):
            goto(i * k, j * k)
            dot(3, "Red")

    done()

def f7():

    old=1024*960*log2(16384)*400/(2**23)
    print (old,log2(16384))
    # old=640*480*16 #размер старой фото
    # new=1280*960*24 #размер новой фото
    # v_old=old*12/1  #скорость канала  бит в сек
    # v_new=v_old*2  # скорость канала после увеличесния в два раза
    # print (v_old/old) #кол-во старых фото на старой скорости в сек
    # print (v_new/new) #кол-во новых фото на новой скорости в сек



def f8():

    s=list("ГРАНИТ")
    s.sort()
    # print(tuple("ТАРА"))

    print (s)
    # скажем enumerate начинать нумерацию с 1
    for i,v in enumerate(product(s,repeat=6),1):
        # v="".join(v)
        if (v[0]!='А' and v[0]!='И' and v[0]!='Г') and v.count('А')==1 and i%2==1:
            print (i,v)





def f9():
    ts=time()
    with open("9.txt") as f:
        a=[]
        cnt=0
        for s in f:
            s=list(map(int,s.split()))
            # print (s)
            m=[s.count(i) for i in set(s)]
            # print (m)

            m.sort()
            if m==[1,1,1,1,3] and s.count(max(s))==1:
                cnt+=1
                print (s,cnt)
        print (time()-ts)


def f8_1():
    ts=time()
    with open("8.txt") as f:
        a=[]
        cnt=0
        for s in f:
            s=list(map(int,s.split()))
            a.append(s)

        # транспонируем массив
        ta=[list(row) for row in zip(*a)]

        # создаем словарь вхождений чисел
        td=[]
        for m in ta:
            di={k:m.count(k) for k in set(m)}
            td.append(di)

        # или в одну строчку
        # td=[{k:m.count(k) for k in set(m)} for m in ta]

        for m in a:
            k=[]


            for i,v in enumerate(m):

                if m.count(v)==1:

                    if td[i][v]>=335+1: #встречается в столбце словаря  не менее 335+1 раз
                        if v<sum(m)/len(m): #меньше среднеарифметического строки
                            k.append(v)
            if len(k)==1:
                cnt+=1
        print (cnt)
        print (time()-ts)
        # сравните время выполнение со словарем и без



def f11():
    for N in range(1,2000):
        i=ceil(log2(N))
        sn=ceil((105*i)/8)
        if 65536*sn >=7*(2**20):
            print (N,i,sn)



    # csymb=(26+10)
    # mbit=ceil(log2(csymb)) # кол-во бит на 1 символ
    # print (ceil(mbit*13/8)) #байт на 1 код
    # print (ceil((ceil(log2(60))+ceil(log2(12)))/8)) #байт на срок




def f11_1():
    def f(s):
        while '111' in s:
            s=s.replace('111','22',1)
            s = s.replace('222', '11', 1)

        return s.count('1')
    maxi=-1
    for n in range(100,1000):
        cnt=f('1'*n)
        if cnt>maxi:
            maxi=cnt
            print (n,maxi)



def f12():
    s = bin(2028)[2:]
    s = 'L' + s + "LLLLL"
    q=0
    a=[]

    for i,v in enumerate(s,1):
        print (i,v)
        if v=='L':
            if q==0:
                a.append('L')
                q=1
            elif q==1:
                a.append('0')
                q = 2
            elif q==2:
                a.append('0')
                q = 3
            elif q == 3:
                a.append('L')
                q = 3
                break

        elif v=='0':
            a.append('0')
            q=1
        elif v=='1':
            a.append('1')
            q=1
    s="".join(a[1:-1:])
    print (int(s,2))

def f13():

    ipn=ip_network('190.202.83.62/255.255.252.0',0)
    for ip in ipn:
        print (ip)
    print (190+202+83+254)


def f13_1():
    def f(s,n):
        s=s[::-1]
        k=0
        for i,v in enumerate(s):
            k+=int(v)*(n**i)
        return (k)

    for x in range(39):
        i=f("653071",39)+f("42037",39)+x*(39**2)+x*(39**2)
        if i%14==0:
            print (i//14)
            break

def f14():

    def f(n):
        s=""
        cnt=0
        di=printable[:27]
        while n>0:
            ost=n%27
            n=n//27
            if ost==0:
                cnt+=1
            s=di[ost]+s

        if cnt==6:
            return s
        else:
            return 0


    suma = 3 * (27 ** 9) + 2 * (27 ** 6) + 27 ** 3

    for x in range(27_000 + 1):
        k=suma-x

        if f(k):
            print (f(k),(x))
            break

    # f(suma-10)
    # a=[f(suma-x) for x in range(27_000+1)]
    # print (a)


def f14_1():
    def f(x, a1, a2):
        P = 215 <= x <= 264
        Q = 221 <= x <= 294
        A = a1 <= x <= a2
        return (not(( P ) <= (( (not(A))and(Q)) <=( not(P)))))

    m = []
    d = []
    for x in (215, 264, 221, 294):
        d.append(x)
        d.append(x + 0.01)
        d.append(x - 0.01)

    for a1 in range(1, 300):
        for a2 in range(1, 300):
            if any((f(x, a1, a2) for x in d)) == False:
                # print (a2-a1)
                m.append(a2 - a1)

    print(min(m))

def f15():
    ts=time()
    def f(x, y, A):
            if (((x < A) and (y < A)) or ((x + 4*y) != 78125)):
                return 1
            else:
                print (x,y,A)
                return 0
    k=[]

    with open("15.dmp", "rb") as fr:
        k=load(fr)

    # for x in range(1,78125):
    #     for y in range(1,7825):
    #         n=x+4*y
    #         if n > 78125:
    #             break
    #
    #         if n==78125:
    #             k.append((x,y))
    #
    print (k)
    # with open("15.dmp","wb") as fw:
    #     dump(k,fw)
    A=[i for i in range(1,79000)]
    for a in range(1,79000):
        for x,y in k:
            if a<=x or a <=y:
                A.remove(a)
                break
    print (A[:10])
    print (time()-ts)
    # for a in range(78100,78130):
    #         m=[f(x,y,a) for x in range(1,100) for y in range(78120,78130)]
    #         if all(m):
    #             print (m)


        # if all(f(x, y, a) == 0 for y in range(1, 78130) for x in range((78125-y)//4, 0,-1)):
        #     print(a)
        #     break





        #
        # if all([fa(A,x,y) for x in range(0,int(78125/5)) for y in range(0,int(78125/5))]):
        #     print (A)
        #     break

    # def f5d(n):
    #     return int((n%5==0))
    #
    # with open("15.txt") as f:
    #     a=[]
    #     maxi=-10**20
    #     max321=-1
    #     cnt=0
    #     for s in f:
    #         s=s.strip()
    #         a.append(int(s))
    #         if int(s)%1000==321:
    #             max321=max(max321,int(s))
    #
    #     for a1,a2,a3 in zip(a,a[1:],a[2:]):
    #         if (a1+a2+a3)>max321:
    #             if (f5z(a1)+f5z(a2)+f5z(a3))==2 and (f5d(a1)+f5d(a2)+f5d(a3))>=1:
    #                 maxi=max(maxi,(a1+a2+a3))
    #                 cnt+=1
    #     print (cnt,maxi)


def f16():

    @lru_cache(None)
    def f(n):
        if n >=19:
            return f(n-4)+3580
        else:
            return 6*(g(n-7)-36)

    @lru_cache(None)
    def g(n):
        if n >=248045:
            return n/20+28
        else:
            return g(n+9)-4

    # заполняем кэш
    for i in range(248045,300000):
        g(i)

    for i in range(300000,1,-1):
        g(i)

    for i in range(1,673):
        f(i)
    print (f(673))

    # print(f(6))


def f17():
    def f171(k):
        if 1000<=abs(k)<=9999:
            return 0
        else:
            return 1

    with open("17_25356.txt") as f:
        a=[int(x) for x in f]
        print (len(a))
        cnt=0
        maxi=max([i for i in a if abs(i)%100==30])
        print (maxi)
        n=[]
        for a,b,c in zip(a,a[1:],a[2:]):
            print (a,b,c)
            if ( f171(a)+f171(b)+f171(c) )==3 and (a+b+c)>maxi:
                cnt+=1
                n.append((a+b+c))

        print (len(n),max(n))




def f1921():
    def f(a, m):
        if a  >= 125: return m % 2 == 0
        if m == 0: return 0
        h = [f(a + 2,  m - 1), f(a + 4, m - 1), f(a * 2, m - 1)]

        # для 19 задачи если неудачный ход
        # return any(h) if (m +1) % 2 == 0 else any(h)

        # для 20-21 задачи и (19 задачи для любых ходов)
        return any(h) if (m + 1) % 2 == 0 else all(h)

    print("19:", [s for s in range(1, 124 + 1) if f( s, 2)])
    print("20:", [s for s in range(1, 124 + 1) if (not f( s, 1)) and f( s, 3)])
    print("21:", [s for s in range(1, 124 + 1) if (f( s, 2)) or f( s, 4)])



def f23():
    def f(x, y):
        if x == y:
            return 1
        if x < y or x==36:
            return 0

        return f(x - 3, y) + f(x - 6, y)+ f(x//2,y)


    print(f(86, 53)*f(53,12))



def f24():
    ts=time()
    with open("24_25361.txt") as f:
        a=[]
        s=f.readline()
        print (len(s))
        #
        k=set(list(s))
        # k.remove('A')
        # for c in k:
        #     s=s.replace(c,':')
        # s=s.split(':')
        # print (len(max(s)))
        s=s.replace('2','0').replace('4','0').replace('6','0').replace('8','0')
        s=s.replace('0',':0')
        m=s.split(':')
        # print (m[:100])
        for x in m:
            if x.count('F')>=76:
                print (len(x),x.count('F'))
                a.append(x)
        for x in a:
            cnt=0
            for i,v in enumerate(x):
                if v=='F':
                    cnt+=1
                    if cnt==77:
                        print (x[:i],len(x[:i]))
                        break
        # print (max(a))
        print (time()-ts)
def f25():

    def f25_1(N):
        a=[]
        for i in range(111,N,100):
            if N%i==0 :
                return (N,i)
        return 0
    cnt=0
    for i in range(1_350_050,1_350_200):
        if f25_1(i)!=0:
            print (*f25_1(i))
            cnt+=1
        if cnt==5:
            break


def f26():
    with open("26_25363.txt") as f:
        nach=[]
        kon=[]
        k=[]
        n=int(f.readline())
        for i,s in enumerate(f,1):
            if len(s)>0:
                a=list(map(int,s.split()))
                # print (i,a)
                if a[0]==a[1]:
                    print ("Fuck")
                    break
                if a[0]<a[1]:
                    k.append((a[0],i,1))
                else:
                    k.append((a[1],i,2))



        k.sort()
        print (k[-1])
        for t,n,l in k:
            # print (t,n,l)

            if l==1:
                nach.append((n,t))
            else:
                kon.append((n,t))

        print (nach[-1],kon[-1],len(nach),len(kon))

            # if v[1]==667:
            #     print (i,v)

        # print (nach[:5],kon[:5])
        # print (k)

def f27A():
    data = []

    def centa(clu):
        a = []
        for p1 in clu:
            suma = 0
            for p2 in clu:
                suma += dist(p1, p2)
            a.append([suma, p1])

        return min(a)[1]

    # with open("demo_2025_22_A.txt") as f:

    with open("27_A_25364.txt") as f:
        for s in f:
            m = list(map(float, s.replace(',', '.').split()))
            # print (m)
            data.append(m)

    clusters = []
    while data:

        cl = [data.pop()]

        for p1 in cl:
            sosedi = [p2 for p2 in data if dist(p1, p2) < 1]
            for p2 in sosedi:
                if p2 in data:
                    data.remove(p2)
                cl.append(p2)
        clusters.append(cl)

    print([len(cl) for cl in clusters])

    px = 0
    py = 0
    for cl in clusters:
        cent=centa(cl)
        k=dist((1.0,1.0),cent)
        print (int(k*10000))



    # print (clusters)
    # for cl in clusters:
    #     px += centa(cl)[0]
    #     py += centa(cl)[1]
    #
    # px = px * 10_000 / len(clusters)
    # py = py * 10_000 / len(clusters)

    # print(px // 1, py // 1)

def f27B():
    data = []

    def centa(clu):
        a = []
        for p1 in clu:
            suma = 0
            for p2 in clu:
                suma += dist(p1, p2)
            a.append([suma, p1])

        return min(a)[1]

    # with open("demo_2025_22_A.txt") as f:

    with open("27_B_25364.txt") as f:
        for s in f:
            m = list(map(float, s.replace(',', '.').split()))
            # print (m)
            data.append(m)

    clusters = []
    while data:

        cl = [data.pop()]

        for p1 in cl:
            sosedi = [p2 for p2 in data if dist(p1, p2) < 1]
            for p2 in sosedi:
                if p2 in data:
                    data.remove(p2)
                cl.append(p2)
        clusters.append(cl)

    print([len(cl) for cl in clusters])

    px = 0
    py = 0
    for cl in clusters:
        Q1=0
        Q2=0
        cent=centa(cl)
        for (xy) in cl:
            if dist(cent,xy)<=1.2:
                Q1+=1
            if dist(cent, xy) <= 0.75:
                Q2 += 1
        print (len(cl),Q1,Q2)
        # k=dist((1.0,0.1),cent)
        print (int(Q1),int(Q2))



    # print (clusters)
    # for cl in clusters:
    #     px += centa(cl)[0]
    #     py += centa(cl)[1]
    #
    # px = px * 10_000 / len(clusters)
    # py = py * 10_000 / len(clusters)

    # print(px // 1, py // 1)


f15()