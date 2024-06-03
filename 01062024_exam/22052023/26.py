f=open("26.txt")
n=int(f.readline())
a = [[0] * 10001 for j in range(10001)]
for i in range(n):
    x, y = map(int, f.readline().split())
    a[x][y] = 1
maxi = 0
mini = 0
for i in range(10001):
    count = 0
    m = 0
    for j in range(10001):
        if a[i][j] == 1:
            count += 1
            m = max(count, m)
        else:
            count = 0
    if m > maxi:
        maxi = max(maxi, m)
        mini = i
print(maxi, mini)


