

# 247

def fufa(s,l):

    if '1' not in s and '0' not in s:
        print("!!!!",s, l)
        return s
    else:
        # print(s, l)
        a = {'01': 'A', '100': 'Д', '101': 'К', '10': 'Н', '111': 'О','000':'С'}
        m=""
        for k in a:
            if k in s :
                m=s.replace(k,a[k],1)
                m=fufa(m,l+1)
                if m:
                     return m


a=["100101000","101111100","100111101"]
for s in a:

    print("!",fufa(a[0],0))




