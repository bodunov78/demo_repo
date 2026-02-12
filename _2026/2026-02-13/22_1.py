with open('22.txt') as file:
    processes = {0: 0}
    a=[]
    for line in file.readlines():
        num, time, related = line.split()
        s=line.replace(';',' ')
        m=list(map(int,s.split()))
        print (m)
        a.append(m)
    print(a)
    for m in a:
        processes[m[0]]=m[1]

    print (processes)
            # m.append(processes.get(processes[i], 0))
    for a1,a2,*related in a:
        print (related)
        processes[num] = max([ processes[i] for i in related]) + a2
        # print (num, time, related,processes[num])

    print(max(processes.values()))
