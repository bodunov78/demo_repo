f = open("48447.txt")
n = f.readline()
cubes = sorted([int(i) for i in f], reverse=1)
cklad=[]
while len(cubes)>0:
    block = [cubes.pop(0)]
    for i in range(len(cubes)):
        if (block[-1]-cubes[i])>=5:
            block.append(cubes[i])
            cubes[i]=''
    cubes=[x for x in cubes if x!='']
    cklad.append(block)
print(len(cklad),max(len(c) for c in cklad))


