def fufu(x,a):
    def dela(x,y):
       if (x%y)==0:
           return 1
       else:
           return 0

    return (dela(x,3)<= (not(dela(x,5))) ) or ((x+a)>=90)



for a in range(1,200):
    m=[fufu(x,a) for x in range(1,100)]
    if all(m)==True:
        print (a)