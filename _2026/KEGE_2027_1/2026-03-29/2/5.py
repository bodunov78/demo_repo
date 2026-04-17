from pickle import *
with open("Big_array.bin","rb") as ba:
    b=load(ba)
    b.sort(key=len)
    print (len(b),b[:3])
