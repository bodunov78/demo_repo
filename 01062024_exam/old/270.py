#from math import ceil
#
#f = open("27_B.txt")
#n = int(f.readline())
#sum_tkm=0
#sum_t=0
#t=[]
#pre_sum_t=0
#pre_sum_tkm=0

#for i in range(n):
#    a=list(map(int,f.readline().split()))
#    a[1]=ceil(a[1]/36)
#    t.append(a)
#    sum_tkm+=t[i][0]*t[i][1]
#    sum_t = sum_t + t[i][1]
#    #print (sum_tkm,sum_t,t)
#summ=[]
#for i in range(n):
#    pre_sum_t+=t[i][1]
#    pre_sum_tkm+=t[i][0]*t[i][1]
#    #print(pre_sum_t,pre_sum_tkm)
#    suma=(sum_tkm-2*pre_sum_tkm)+t[i][0]*(2*pre_sum_t-sum_t)
#    summ.append(suma)

#print("Otvet:",min(summ))
