#100000 888888
s1="12345678"
s0="012345678"
cnt=0
for a1 in s1:
    for a2 in s0:
        for a3 in s0:
            for a4 in s0:
                for a5 in s0:
                        for a6 in s0:
                            s=a1+a2+a3+a4+a5+a6
                            s=s.replace('3','1').replace('5','1').replace('7','1').replace('0','2').replace('6','2').replace('8','2')
                            if s.count('4')==1 and s.count('1')==2:
                                cnt+=1

print (cnt)