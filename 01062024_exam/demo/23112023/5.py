def function1(n1='Fine',n2='None'):

    return n1.upper(),n2.lower(),'Чубураха'


def function2(**n):
    print ( n.keys(),n.values())


    # return n[0].upper(),n.lower(),'Чубураха'



a=function2(n2="hkjhkjhk",n1='DSDFFF')
print (a)


# print (function1())