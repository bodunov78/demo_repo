from re import *



s="0123*2300*00*12*002*234"



num=r"([1-9][0-9]*|0{1})"
# numz=r"([1-9][0-9]*|0{1})"

proiz=rf"{num}(\*{num})*"
reg=rf"(?=({proiz}))"
for x in finditer(reg,s):
    print(x.group(1))



    # num=r'[1-9][0-9]*|0'
    # proiz=rf'(({num}\*)*0(\*{num})*)'
    # reg=rf'{proiz}([+*]{proiz})+'
    # m=[len(x.group()) for x in finditer(reg,s)]
    # # k=[]
    # # for x in m:
    # #     if eval(x)==0:
    # #         k.append(len(x))
    # print (max(m))