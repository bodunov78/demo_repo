from itertools import *

# 1 при помощи циклов for и while получить все комбинации слов из cловаря(ABCDEF) длиной 7 сиволов
# 2 при помощи циклов for и while получить все комбинации слов из cловаря(ABCDEF) длиной 7 сиволов ,
# но любой символ не может встречаться больше 2 раз
# 3 при помощи циклов for и while получить все комбинации слов из cловаря(ABCDEF) длиной 7 сиволов,
#  одинаковые символы могут встречаться не более трех раз и стоять могут только рядом
#  4 при помощи циклов for и while получить все перестановки слов (ABCDEF)
#  5 используя генераторы списков получить массив числел кратных 7 и не кратных 5
#  6 используя генераторы списков получить массив 20 кортежей пар чисел являющимися решениями
#  диофантового уравнения 7x+13y=40 .(Пример ( [(1,2),(2,3),....])


# 1 при помощи циклов for и while получить все комбинации слов из cловаря(ABCDEF) длиной 7 сиволов
def fu1():
    # при помощи циклов for и while получить все комбинации слов из cловаря(ABCDEF) длиной 7 сиволов ,

    s = "ABCDEF"
    for s1 in s:
        for s2 in s:
            for s3 in s:
                for s4 in s:
                    for s5 in s:
                        for s6 in s:
                            for s7 in s:
                                st=s1 + s2 + s3 + s4 + s5 + s6 + s7
                                print(st)


def fu11():
    s = "ABCDEF"
    for i in product(s,repeat=7):
        print ("".join(i))



# 2 при помощи циклов for и while получить все комбинации слов из cловаря(ABCDEF) длиной 7 сиволов ,
# но любой символ не может встречаться больше 2 раз

def fu2():
    # при помощи циклов for и while получить все комбинации слов из cловаря(ABCDEF) длиной 7 сиволов ,
    #но любой символ не может встречаться больше 2 раз

    s = "ABCDEF"
    for s1 in s:
        for s2 in s:
            for s3 in s:
                for s4 in s:
                    for s5 in s:
                        for s6 in s:
                            for s7 in s:
                                st=s1 + s2 + s3 + s4 + s5 + s6 + s7
                                if st.count(s1)<=2 and st.count(s2)<=2 and st.count(s3)<=2 and st.count(s4)<=2 and st.count(s5)<=2 and st.count(s6)<=2 and st.count(s7)<=2:
                                    print(st)

# 3 при помощи циклов for и while получить все комбинации слов из cловаря(ABCDEF) длиной 7 сиволов,
#  одинаковые символы могут встречаться не более трех раз и стоять могут только рядом

def fu30():
    # при помощи циклов for и while получить все комбинации слов из cловаря(ABCDEF) длиной 7 сиволов ,
    #одинаковые символы  могут  встречаться  не более трех  раз  и  стоять  могут  только рядом
    # ошибка
    s = "ABCDEF"
    for s1 in s:
        for s2 in s:
            for s3 in s:
                for s4 in s:
                    for s5 in s:
                        for s6 in s:
                            for s7 in s:
                                st=s1 + s2 + s3 + s4 + s5 + s6 + s7
                                if (st.count(s1)<=3 and st.count(s1)==3) or (st.count(s2*3)==1 and st.count(s2)==3) or (st.count(s3*3)==1 and st.count(s3)==3) or (st.count(s4*3)==1 and st.count(s4)==3) or (st.count(s5*3)==1 and st.count(s5)==3) or (st.count(s6*3)==1 and st.count(s6)==3) or (st.count(s7*3)==1 and st.count(s7)==3):
                                    print(st)


def fu31():
    #при помощи  циклов  for и while получить все комбинации слов из cловаря(ABCDEF) длиной 7 сиволов,
    #одинаковые символы  могут  встречаться  не более трех  раз  и  стоять  могут  только рядом

    s = "ABCDEF"
    i=0
    l=[]
    for s1 in s:
        for s2 in s:
            for s3 in s:
                for s4 in s:
                    for s5 in s:
                        for s6 in s:
                            for s7 in s:
                                st=s1 + s2 + s3 + s4 + s5 + s6 + s7
                                #st.count(s1)<=3 повторяющихся символов не больше 3
                                #st.count(s7*st.count(s7))==1 все повторяющиеся символы вместе
                                if (st.count(s1)<=3 and st.count(s2)<=3 and st.count(s3)<=3 and st.count(s4)<=3 and st.count(s5)<=3 and st.count(s6)<=3 and st.count(s7)<=3) and st.count(s1*st.count(s1))==1 and st.count(s2*st.count(s2))==1 and st.count(s3*st.count(s3))==1 and st.count(s4*st.count(s4))==1 and st.count(s5*st.count(s5))==1 and st.count(s6*st.count(s6))==1 and st.count(s7*st.count(s7))==1:
                                    i+=1
                                    l.append(st)
    print(l,len(l))


def fu32():
    #при помощи  циклов  for и while получить все комбинации слов из cловаря(ABCDEF) длиной 7 сиволов,
    #одинаковые символы  могут  встречаться  не более трех  раз  и  стоять  могут  только рядом

    s = "ABCDEF"
    a=["".join(x) for x in product(s,repeat=7) if all(x.count(y)<=3   for y in set(x))]
    m=[x for x in a if (all(x.count(y*x.count(y))==1 for y in set(x)))]
    # print (a,len(a))
    print(m,len(m))

def fu4():
    # при помощи циклов for и while получить все перестановки слов (ABCDEF)
    s = "ABCDEF"
    i=0
    for s1 in s:
        for s2 in s:
            for s3 in s:
                for s4 in s:
                    for s5 in s:
                        for s6 in s:
                            st=s1 + s2 + s3 + s4 + s5 + s6

                            if (st.count(s1)==1 and st.count(s2)==1 and st.count(s3)==1 and st.count(s4)==1 and st.count(s5)==1 and st.count(s6)==1):
                                i+=1
                                print(st,i)


def fu41():
    s = "ABCDEF"
    for i in permutations(s):
        print("".join(i))



#  5 используя генераторы списков получить массив числел кратных 7 и не кратных 5

def fu5():
    arr=[x for x in range(1000) if x%7==0 and x%5!=0]
    print(arr)

#  6 используя генераторы списков получить массив 20 кортежей пар чисел являющимися решениями
#  диофантового уравнения 7x+13y=40 .(Пример ( [(1,2),(2,3),....])

def fu6():

    arr = [(x,y) for x in range(-100,160) for y in range(-1000,1000) if 7*x+13*y==40]
    print(arr,'\n',len(arr))


def fu61():
    arr = [(13*n+2,2-7*n) for n in range(0,20)]
    print(arr,'\n',len(arr))


fu61()
# fu32()

