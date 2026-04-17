from math import *
n=200
lg=ceil(log2(n))
k=2**(lg)-1
print (k)
print (bin(n)[2:])
b1=bin(n)[2:]
b2=bin(n^k)[2:].zfill(lg)
print (*list(b1),sep='\t')
print (*list(b2),sep='\t')
# print (bin(n^k)[2:].zfill(lg))