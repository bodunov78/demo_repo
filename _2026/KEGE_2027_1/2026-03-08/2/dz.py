# #48387
for x in range(11):
    for y in range(11):
        a=int("03410",11) +x*(11**4)+y+int("56010",19)+x*(19**2)+y
        if a%305==0:
            print (a//305)

from string import *

for x in printable[:11]:
    for y in printable[:11]:
        a=int(f"{x}341{y}",11)+int(f"56{x}1{y}",19)
        if a%305==0:
            print (a//305)

for x in range(11):
    for y in range(11):
        a=x*(11**4)+3*(11**3)+4*(11**2)+1*11+y +5*19**4+6*19**3+x*19**2+1*19+y
        if a % 305 == 0:
            print(a // 305)

print(219&240)