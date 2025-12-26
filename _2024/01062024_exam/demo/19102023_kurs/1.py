a="12344;5"

# arr=list(map(int,a.split(";")))
# print (arr)

b=[1,2,-3,4,5]
c=[6,7,88,9]

# b+=c
c+=b



m="".join(str(c))
print(m)
# print(c)
# c.sort()
# print(c)
# print(c[0],c[-1])
# c=c[1:-1]
# print(len(c),c[6])
print (sum(c))

# m="".join(s)
# print(s,type (s))


s=" 1+2+3 -     344 + 5 - 6 +7 -99\n\n "
while '  ' in s:
     s=s.replace('  ',' ')

print (s)
s=s.strip()
print (s)

s=s.replace('+',' ')
s=s.replace('-',' -')
s=s.replace('- ',' -')
s=s.replace('  ',' ')
s=s.replace('  ',' ')

m=s.split(' ')
print(m)



# m=a.split(',')
# k=list(map(float,m))
# print(k[2],type(k[2]))
#
#
#
#
# print(m,type(m),m[2],type(m[2]))
# print(int(m[2])+5)






# a=[91,82,3,4,5,6,2,3,4]
# print (min(a),max(a),len(a),sum(a))
# print(a,sorted(a),sorted(a,reverse=1))
# a.sort()
# print(a)
# a.sort(reverse=1)
# print (a)
# print (set(a))
# a=list(set(a))
# print(a)
#
# s=" 1, 2, 3, 4,5,6,7,8,90   \n\n"
# print (s,len(s))
# s=s.strip('\n')
#
#
#
# #s=s.strip()
# print(s,len(s))
# print (s)
# print("abc")
#
#
# # m=list(s.split(','))
# # print(m)