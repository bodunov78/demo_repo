#3
def fufu(s,e):
    if s>e: return 0
    elif s==e : return 1
    else: return fufu(s+1,e)+fufu(s*2,e)

print (fufu(1,10)*fufu(10,21)*fufu(21,30))