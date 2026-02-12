
a=dict()
a={"aaa":123,"bbb":222}

a['sss']=5

print (a)
# выводит все ключи из словаря
for k in a.keys():
    print (k)
# выводит все значения из словаря
for v in a.values():
    print (v)
# выводит ключ_пробел_значения из словаря
for k,v in a.items():
    print (k,v)
