

# 247

def fufa(s,l):

    if '1' not in s and '0' not in s:
        # print("!!!!",s, l)
        return s
    else:
        # print(s, l)
        a = {'10': 'A', '001': 'Г', '00': 'М', '010': 'К', '1100': 'Ю'}
        for k in a:
            if k in s :
                m=s.replace(k,a[k],1)
                print (f"S-M {s} :{m}")
                m=fufa(m,l+1)
                if m:
                    return m



s="001000001110001010"
k=fufa(s,0)
print("!",k)




