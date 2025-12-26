d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]


def get_line_list(d, a=[]):
    for  i,x in enumerate(d):

        if type(x)!=list:
            # print ("aaa",x)
            a.append(x)
        else:
            a=get_line_list(x,a)
    #print (a)
    return a



get_line_list(d,[])
# здесь продолжайте программу