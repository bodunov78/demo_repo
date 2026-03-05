f=open('Название_файла.txt','r')
a=f.read().split()
f.close()
print(len(a))