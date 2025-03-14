

def min_arr(a,mn,mx):
    if mx==0:
        a1=min(a,key=lambda x: x[mn-1])[mn-1]
        a2 = [r for r in a if r[mn-1] == a1]
        a3 = min(a2,key=lambda x: x[(0-mn)%mn])
        print(a1, a2, a3)
    else:
        a1 = min(a, key=lambda x: x[mn - 1])[mn - 1]
        a2 = [[r[0], r[1]] for r in a if r[mn-1] == a1]
        a3 = max(a2,key=lambda x: x[mx-1])
        print(a1, a2, a3)

def max_arr(a,mx,mn):
    if mn==0:
        a1=max(a,key=lambda x: x[mx-1])[mx-1]
        a2 = [r for r in a if r[mx - 1] == a1]
        a3 = max(a2,key=lambda x: x[(0-mx)%mx])
        print(a1, a2, a3)
    else:
        a1 = max(a, key=lambda x: x[mx - 1])[mx - 1]
        a2 = [r for r in a if r[mx-1] == a1]
        a3 = min(a2,key=lambda x: x[mn-1])
        print(a1, a2, a3)


def sumarr(a,b,r):
    if r==0:
        a.sort(reverse=1)
        b.sort(reverse=1)

        result = [sum(i) for i in zip(a, b)]
    else:
        a.sort(reverse=1)
        b.sort()
        result = [sum(i) for i in zip(a, b)]

    result.sort(reverse=1)
    return result



a=[[20,30],[30,20],[40,50],[20,1],[40,1],[-1,20]]

#print(min_arr(a,2,1))
print(min_arr(a,1,0))

#
# a1=max(a)[0]
# a2=[[r[0],r[1]] for r in a if r[0] == a1]
# a3=min(a2)
# print(a1,a2,a3,max(a))



#a=[[10,20],[10,30],[10,40],[8,40]]
#print(min(a,key=lambda tup: tup[1]))

#print(min(a,key=lambda tup: tup[1]))
#min(a,)
#print(min(a))
