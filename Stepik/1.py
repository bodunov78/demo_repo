arr2=[[1, 0, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
arr=arr2[:]

for i in range(5):
    arr[i].insert(0,0)
    arr[i].append(0)

arr.insert(0,[0,0,0,0,0,0,0])
arr.append([0,0,0,0,0,0,0])

flag = 1
for i in range(1, 6):
    for j in range(1, 6):
        if arr[i][j] == 1:
            if arr[i - 1][j - 1] == 0 and arr[i][j - 1] == 0 and arr[i + 1][j - 1] == 0 and arr[i - 1][j] == 0 and \
                    arr[i + 1][j] == 0 and arr[i - 1][j + 1] == 0 and arr[i][j + 1] == 0 and arr[i + 1][j + 1] == 0:
                flag = 1
            else:
                flag = 0
                break
    if flag==0:
        break
if flag == 1:
    print("ДА")
else:
    print("НЕТ")

print (arr,"\n",arr2)

d={}
d["house"] = ['дом', 'жилище', 'хижина']

d[1] = 'one'

# d[[True]] = 'истина'

# d[[1, 2, 3]] = 123

d[True] = 'истина'

d['dict'] = {'one': 1, 'two': 2}

d[5.6] = 5.6
d.remove('1')