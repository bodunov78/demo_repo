#1
def fufu(s,e):
    if s>e: return 0
    elif s==e : return 1
    else: return fufu(s+1,e)+fufu(s*3,e)

print (fufu(1,22)*fufu(22,70))