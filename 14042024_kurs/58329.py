#1
with open("58329.txt") as f:
    s=f.readline().strip()
    ns=""


    maxi=-10**19
    for i in range(len(s)-2):
        if int(s[i])+int(s[i+1])>int(s[i+2]):
            if len(ns)==0:
                ns=s[i:i+3]
            else:
                ns+=s[i+2]
        else:
            maxi=max(len(ns),maxi)
            print(ns,maxi)
            ns=""
