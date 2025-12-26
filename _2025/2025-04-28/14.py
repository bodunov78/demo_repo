# #1:12
# for x in range(1,25):
#     s=int('11355',25)*25**3+x**2+int('12',25) +int('135',25)*25**3+x*25**2+int('21',25)
#     if s%24==0:
#         print(x,s/24)
# #1:15
from string import *
print(printable[:25])
for x in printable[:25]:
    # print (x)
    s1=f"11353{x}12"
    s2=f"135{x}21"

    k=int(s1,25)+ int(s2,25)
    if k%24==0:
        print (x,k/24)