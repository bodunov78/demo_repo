def find_divisors(start, end, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for num in range(start, end + 1):
            div = []
            
            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    div.append(i)
                    if i*i != num:
                        div.append(num // i)
            
            
            div.sort()
            
           
            f.write(f"{num}: {', '.join(map(str, div))}\n")


find_divisors(1001, 2000, 'delit.txt')

