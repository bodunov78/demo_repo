#4_1

def fufu(s,e):
    if s>e or s==26: return 0
    elif s==e : return 1
    else: return fufu(s+1,e)+fufu(s*2+1,e)

print (fufu(1,27))