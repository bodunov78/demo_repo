# 1 3 5 7 9 11 13 15

for i in ("1 лев","сова ",10**10,7,9,11,13 ,15):
    print (i*1)
    print ("не Сова ", "Не -лев")

for i in range(1,20+1,2):
    print (i)

i=10

while i < 20:
    print (i,"Осёл!!!")
    i=i+2

while True:

    print (i, "Бегемот")
    i+=10
    if i > 10**6:
        print ("Давай, выходи.....")
        break

    print(i%6)



