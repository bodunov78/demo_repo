from math import *
a=set()
suma_c=-1
mini=10**20
flag=0
cnt=0
for a3 in range(ceil(100_000/7),100000//8,-1):
    for a6 in range(100_000-a3*7,1,-1):
        if flag==1:
            flag=0
            break
        for a9 in range(100_000-a6*8,1,-1):
            suma_c=a3 + a6 + a9
            if suma_c > 300 :

                sum_N = a3 * 3 + a6 * 6 + a9 * 9
                sum_S = a3 * 7 + a6 * 8 + a9 * 3
                if sum_S>=100_000 and (a3+a9)>=300 and mini>(sum_N+sum_S):
                    # print (sum_N+sum_S)
                    mini=min(mini,sum_N+sum_S)
                    # a.add((mini))
                    cnt+=1
                    if cnt%1000==0:
                        print (mini,a3,a6,a9)

                elif sum_S<100_000:
                    flag=1
                    break
            else:
                flag=1
                break

print (mini)