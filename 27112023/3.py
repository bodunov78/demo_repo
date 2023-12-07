def fact(s, n):
    if len(s) > 0:
        s.append(s[-1] + (s[-2] ))
        # s.append(s[-1] *(len(s)+1))

    else:
        s.append(1)
        s.append(1)
   return s, n
s = [1,0,1]


for n in range(1, 7):
    print(fact(s,n))
