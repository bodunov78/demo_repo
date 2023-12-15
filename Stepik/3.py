def verify(a):
    suma=[0]*len(a)
    print (suma)
    for x in a:
        for i in range(len(a)):
            suma[i]=suma[i]+x[i]

        for i in range(len(a)-1):
            if suma[i]*suma[i+1]>=1:
                return False

        if max(suma)>1 :
            return False
        suma=x.copy()

    return True



print(verify([[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]))