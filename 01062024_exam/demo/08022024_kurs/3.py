def fu(a,d):
    m=list(a)
    mc=[]
    md=[]
    s=""
    for i in m:
        md.append(ord(i))
        mc.append(chr(ord(i)+d))

    s="".join(mc)
    return s

fu(fu(fu(a)))

print (chr(ord('М')))
s="мама мыла раму"
print(fu(fu(s,13),-13))