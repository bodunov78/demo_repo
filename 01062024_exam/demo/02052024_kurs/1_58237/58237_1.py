#58237

# Сколько существует различных четырёхзначных чисел, записанных в семеричной системе счисления,
# в записи которых цифры следуют слева направо в строго убывающем порядке?

















cnt=0
for i in range(10**3,10**4):
    s=str(i)
    if '9' in s or '8' in s or '7' in s:
        continue
    else:
        cnt+=1
        print (i,cnt)














#
#
#
#
#
#
# s=("0123456")
# cnt=0
# for a1 in s:
#     for a2 in s:
#         for a3 in s:
#             for a4 in s:
#                 if a1 > a2 > a3 >a4:
#                     ss=a1+a1+a3+a4
#                     cnt+=1
#                     print (ss,cnt)
