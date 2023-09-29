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


def fu3():
    # при помощи циклов for и while получить все комбинации слов из cловаря(ABCDEF) длиной 7 сиволов ,
    #но любой символ не может встречаться больше 2 раз
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


def fu4():
    #при помощи  циклов  for и while получить все комбинации слов из cловаря(ABCDEF) длиной 7 сиволов,
    #одинаковые символы  могут  встречаться  не более трех  раз  и  стоять  могут  только рядом

    s = "ABCDEF"
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
                                    print(st)



fu4()