from string import printable

for x  in printable[:12]:
    a=f"154{x}3"
    b=f"1{x}365"
    i=int(a,12)+int(b,12)
    if i%13==0:
        print (i//13)