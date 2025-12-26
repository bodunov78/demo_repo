#5
def fufu(s,e,a):
    if s>e+12 : return 0
    elif s==e : return 1

    else:
        if a==0:
            return fufu(s-1,e,1)+fufu(s+3,e,0)+fufu(s*2,e,0)
        else:
            return  fufu(s + 3, e,0) + fufu(s * 2, e,0)
print (fufu(3,12,0))