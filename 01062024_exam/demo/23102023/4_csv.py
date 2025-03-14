file= open("107_9_utf8_csv_unicode1.csv", encoding="utf-8-sig")
# file= open("107_9_utf8_csv_unicode1.csv")

for x in file:
    x=x.strip()
    #print (x,type(x))
    a = list(map(int, x.split(";")))
    print(a)


    # with open("107_9_utf8_csv_unicode1.csv",encoding="utf-8-sig") as file:
    # with open(path, encoding="utf-8-sig") as file:

        # with open("107_9_1251_csv_utf8.csv", encoding="utf-8") as file: #ValueError: invalid literal for int() with base 10: '\ufeff17'

        # s = file.readline()
        #a = list(map(int, s.split(';')))
        # a=reader(file,delimiter=";")
        import csv
        a = csv.reader(file, delimiter=";", quotechar=' ')

        # a = csv.reader(file, qu)

#         for x in a:
#             print(x)
#         #print(a)
#         # print(s)
#         # print(0/0)
# except:
#     print("ERROR")
#
