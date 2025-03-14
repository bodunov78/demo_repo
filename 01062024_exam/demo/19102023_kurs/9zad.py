# прочитать csv и засунуть в массив
with open("1_9.csv","r") as file:
    for x in file:
        a=list(map(int,x.split(';')))
        if len(a) == len(set(a)):
            print(a)



