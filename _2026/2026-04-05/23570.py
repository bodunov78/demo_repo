f = open('26_23570_2.txt')
N, K = [int(x) for x in f.readline().split()]
uch = [int(f.readline()) for i in range(N)]

sneg = [10**20] * 1001
for i in range(K):
    m, p = [int(x) for x in f.readline().split()]
    sneg[m] = min(sneg[m], p)

sneg = [[i, sneg[i]] for i in range(1, 1001)]
sneg.sort(key=lambda x: [x[1], x[0]])

mp = []
mm = []

for x in uch:
    for m, p in sneg:
        if m >= x:
            mm.append(m)
            mp.append(p)
            break

print (sneg[:10])
print(sum(mp), max(mm))