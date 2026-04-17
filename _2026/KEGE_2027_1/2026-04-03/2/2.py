lines = [list(map(int,s.split())) for s in open('55596.txt')]
d={}
for line in lines:
    for n in line:
        d[n]=d.get(n,0)+1
goodlines = [line for line in lines if any([line.count(n)==1 and d[n]==46 for n in line])]
print(len(goodlines))