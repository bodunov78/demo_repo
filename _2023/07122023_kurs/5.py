N=int(input())
def frog(N):
    if N==0:
        return 1
    elif N<0:
        return 0
    else:
        return frog(N-1)+frog(N-2)


print(frog(N))