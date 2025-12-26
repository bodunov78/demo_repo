#4_2

def fufu(s,e):
    if s>e : return 0
    elif s==e : return 1
    else: return fufu(s+1,e)+fufu(s*2+1,e)

print (fufu(1,27)-fufu(1,26)*fufu(26,27))