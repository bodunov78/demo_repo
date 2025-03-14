def fu1(s,e,cmd):
    #print(s,e,cmd)
    if s>e or len(cmd)>5:
        return ""
    elif s==e :
        return cmd
    else:
        # print(s%2)
        return fu1(s +1, e, str(cmd) + '1') + fu1(s**2, e, str(cmd) + '2')



print(fu1(3,84,""))