n=1024*280
i=280*1024*8/n
i=i+3
print (i)

for b in range(1,20):
    i=b+3
    if (1024*280*i)<=(280*1024*8):
        print (2**b)
