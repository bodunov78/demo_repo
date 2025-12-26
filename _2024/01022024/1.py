s='01234567890abcdef'


for i  in s:
    for j in s:
        for k in s:
            for n in s:
                print (i,j,k,n)


for x in range(1000,10000):
    y=str(x)
    if y[3]=='1' or y[3]=='2' or y[3]=='3' or y[3]=='4':
        print (y)



    Вывести все 4х значные 16-ричные числа
    (числа в алфавите которых встречаются 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F)