#Составляют 5-буквенные слова из букв слова ПЯТНИЦА. Найти количество слов,
# которые не начинаются с Н и в которых есть только одна буква Я. Буквы в слове могут повторяться.

s="ПЯТНИЦА"
s1="ПЯТИЦА"

cnt=0
for a1 in s1:
    for a2 in s:
        for a3 in s:
            for a4 in s:
                for a5 in s:
                    m=a1+a2+a3+a4+a5
                    if m.count('Я')==1:
                        cnt+=1
                        print(m,cnt)



