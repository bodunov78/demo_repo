# with open("107_9_utf8_csv_unicode1.csv",encoding="utf-8-sig") as file:
# with open("107_9_utf8_csv_unicode1.csv") as file:
try:
    #with open("107_9_1251_csv.csv") as file:
    with open("107_9_utf8_csv_unicode1.csv",encoding="utf-8-sig") as file:

        # with open("107_9_1251_csv_utf8.csv", encoding="utf-8") as file: #ValueError: invalid literal for int() with base 10: '\ufeff17'

        s = file.readline()
        a = list(map(int, s.split(';')))
        #print(a)
        print(s)
        print(0/0)
except:
    print("ERROR")

