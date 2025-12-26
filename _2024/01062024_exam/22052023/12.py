for one in range(0,55):
    for two in range(0,55):
        for three in range(0,55):
            x='0'+'1'*one+'2'*two+'3'*three+'0'
            while not('00' in x):
                x=x.replace('01','210',1)
                x=x.replace('02','320',1)
                x=x.replace('03','3012',1)
            if x.count('1')==26 and x.count('2')==54 and x.count('3')==48:
                print(one+two+three+2)