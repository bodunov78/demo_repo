d=dict()
with open("mumu.txt", encoding="utf-8-sig") as file:
    for s in file:
        a=list(s.lower().replace(',','').replace('!','').replace('?','').replace('.','').replace(';','').replace('-','').replace('  ',' ').strip().split())
        for x in a:
            d[x]=d.get(x,0)+1


# print (d)

# print (d.keys())
# print(d.values())
maxi=0
for keys,val in d.items():
      if val>maxi:
        print (keys,val)
        maxi=val
# #
# sorted_dict = dict(sorted(d.items(), key=lambda x: x[1],reverse=1))
# print (sorted_dict)
#
# m=[[a,b] for a in range(30,20,-1) for b in range(20,10,-1)]
# print (m)
# print(sorted(m, key=lambda  x:x[1],reverse=1))