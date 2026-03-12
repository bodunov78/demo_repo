a={"a":10,"b":20}
print (a['a'])
b={1:"ABC",2:"CDE","ONE":"DFGHJK234"}
print (b['ONE'])
print (b.keys())
print (b.values())

# перебирает ключи и по нему
# получает значение из словаря
for k in b.keys():
    print(k,b[k])

# перебирает значения из словаря
for v in b.values():
    print (v)

# перебирает ключи и значения из словаря
for k,v in b.items():
    print (k,v)

b['dog']="собака"
print (b)
b[123]="Moscow"
print (b)