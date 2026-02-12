with open('22.txt') as file:
    processes = {"0": 0}

    for line in file.readlines():
        num, time, related = line.split()
        processes[num] = max([processes[i] for i in related.split(";")]) + int(time)
        print (num, time, related,processes[num])

    print(max(processes.values()))
