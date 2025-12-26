f=open("24_demo.txt")
a=f.readline()
print (len(a))
a=a.replace('XY','X:Y').replace('YX','Y:X').replace('XZ','X:Z').replace('ZX','Z:X').replace('YZ','Y:Z').replace('ZY','Z:X')

c=[len(x) for x in m]
print(max(c),m)
