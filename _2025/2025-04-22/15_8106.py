# 14:07

def dela(x,y):
    if x%y==0:
        return 1
    else:
        return 0

def f(x, A):
    return ((not (dela (x, A))) <= (dela (x, 6) <= (not (dela (x, 4)))))

for A in range(1,1000):
    m=[f(x,A) for x in range(1,1000)]
    if all(m):
        print (A)

# 14:21