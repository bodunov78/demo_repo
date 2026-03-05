a = []
for i in range(-10000, 0):
    if i % 15 == 0:
        while len(a) < 100:
            a.append(i)
            break
print(a)
