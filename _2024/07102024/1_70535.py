from itertools import *


def fu0():
    count = 0
    for s in product("0123456789AB", repeat=5):
        if s.count("7") == 1 and s[0] != "0":
            if s.count("9") + s.count("A") + s.count("B") <= 3:
                count += 1
    print(count)


def fu1():
    count = 0
    di="0123456789AB"
    for s in product(di, repeat=5):
        m=[s.count(x) for x in di]
        if s[0]!='0' and m[7]==1 and sum(m[9:])<=3:
            count+=1
            print(s,m,count)


        # if s.count("7") == 1 and s[0] != "0":
        #     if s.count("9") + s.count("A") + s.count("B") <= 3:
        #         count += 1
    print(count)





fu1()