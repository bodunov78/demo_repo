
def fufa(s,l):

    if '1' not in s and '2' not in s and '3' not in s:
        print("!!!!",s, l)
        return s
    else:
        print(s, l)
        a = {'31': 'К', '21': 'Л', '13': 'М', '321': 'П', '1': 'О','2':'И'}

        for k in a:
            if k in s :
                m=s.replace(k,a[k],1)
                return fufa(m,l+1)



s="121213321"

print (fufa(s,0))




