with open("1.txt","w+",encoding="utf-8" ) as f:
    for i in range(1,127):
        print (f"{chr(i)}{i}",end="\n",file=f)
    # print  ("aaa",end="",file=f)
    f.write("aaaa")