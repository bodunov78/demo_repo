def fu(a,d):
    s=""
    for i in a:
        s+=chr((ord(i)+d))

    return s



s="мама мыла раму"
print(fu(fu(s,13),-13))


print (13^9)
print (13^4)
print (9^4)