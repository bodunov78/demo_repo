min=30000
for a1 in range(1,100):
    for a2 in range(1,100):
        if all((( 17 < x < 54)<=(((37 < x< 83) and not( a1 < x < a2))<=(not(17< x < 54)))) for x in range (1,100)) and (a2-a1) < min:
            min=a2-a1
print(min)