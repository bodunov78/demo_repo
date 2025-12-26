f = open("27B.txt")
n = int(f.readline())
elems = [0 for i in range(n)]
answers = [0 for i in range(n)]
sum = 0
rightSum = 0
leftSum = 0
for i in range(0, n):
    elems[i] = int(f.readline())
for i in range(0, n):
    elems[i] = elems[i] * 3
for i in range(1, n // 2):
    sum = sum + elems[i] * i + elems[n - i] * i
    rightSum = rightSum + elems[i]
    leftSum = leftSum + elems[n - i]
if n % 2 == 0:
    sum = sum + elems[n // 2] * n // 2
else:
    sum = sum + elems[n // 2] * n // 2 + elems[n - n // 2] * n // 2
answers[0] = sum
for i in range(1, n):
    answers[i] = answers[i - 1] + leftSum + elems[i - 1] - rightSum - elems[(i + (n // 2) - 1) % n]
    rightSum = rightSum - elems[i] + elems[(i + (n // 2) - 1) % n]
    leftSum = leftSum - elems[(i - (n // 2)) % n] + elems[i - 1]
print(min(answers))
