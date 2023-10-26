a={1,2,3,4,5,6,7,7}
# c=[1,2,3,4,5]
# if len(c) == len(set(c)):
#     print ("ok")
# else:
#     print ("FUCCC")
#
#
# print (len(c),len(set(c)))



# print (a)
# a.add(88)
# a.add(88)

# print (a)
a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
# a <5

# a>1
#a=set(range(20,30+1))
#b=set(range(-10,5))
#print (set(a|b)) # U
#print (a&b) # n
#print (set(b-a)) #A- A&B
# print (set(b-a)) #B-A&B
print(set(a^b))   # AuB - AnB
#
# print (a,b)


# a.add(100)
# print(a)
# a.discard(1)
# print(a)
# print (a&b)


# c=set(range(1,100))
# d=set(range(-1*10**6,20+1))
# print (len(d))
# print (c&d)

s={}
s["hello"]="Привет,здравствуй"
s["hello"]="здравствуй"
print(s["hello"])
s="qwertyuwertywertqwer"
sl={}
for c in set(s):
    # print (c, s.count(c))
    sl[c]=s.count(c)
print (sl)
