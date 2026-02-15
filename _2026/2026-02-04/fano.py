code = {'А':'00','Б':'01','В':'100','Г':'1100'}
words = list(code.values())
print (words)
lengths = [2,3,4,5,6]

for l in lengths:
    for i in range(2**(l-1), 2**l):

        w = bin(i)[2:].zfill(l)
        print (w)
        if w in words: continue
        if any(w.startswith(c) or c.startswith(w) for c in words):
            print(w)

            