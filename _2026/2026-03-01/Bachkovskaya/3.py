n = 127
'''
# Способ 1
print(bin(n))
'''
# Способ 2
res = ""
dv=n
while dv > 0:
    res = str(dv% 2) + res
    dv//= 2
print(res)
