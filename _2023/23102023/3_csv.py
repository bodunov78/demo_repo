# with open("107_9_utf8_csv_unicode1.csv",encoding="utf-8-sig") as file:
# with open("107_9_utf8_csv_unicode1.csv") as file:
# path = r'C:\Users\u47-01\PycharmProjects\demo_repo\23102023\107_9_utf8_csv_unicode1.csv'
# path = 'C:\Users\u47-01\PycharmProjects\demo_repo\23102023\107_9_utf8_csv_unicode1.csv'
path = 'C:\\Users\\u47-01\\PycharmProjects\\demo_repo\\23102023\\107_9_utf8_csv_unicode1.csv'

print(path)
from csv import reader
# file=open("107_9_1251_csv_utf8.csv", encoding="utf-8-sig")

try:
    with open("107_9_1251_csv_utf8.csv", encoding="utf-8-sig") as file:
        n=int(file.readline())

        for i in range(n):
            x = file.readline()
            print(x)
    #     x=file.readlines()
    #     print(x)
    # #     for s in file:
    # # # print (s)
    # #         a = list(map(int, s.split(';')))
    # #         a.sort()
    # #         print(a)
    # #         print (int("abc"))

except:
     print ("Errooorrr")



    # with open("107_9_utf8_csv_unicode1.csv",encoding="utf-8-sig") as file:
    # with open(path, encoding="utf-8-sig") as file:

        # with open("107_9_1251_csv_utf8.csv", encoding="utf-8") as file: #ValueError: invalid literal for int() with base 10: '\ufeff17'

        # s = file.readline()
#         for s in file:
#             # print (s)
#             a = list(map(int, s.split(';')))
#             a.sort()
#             print(a)
#
#         # a=reader(file,delimiter=";")
#         # a = reader(file, delimiter=";", quotechar=' ')
#         # a = csv.reader(file, qu)
#
#         # for x in a:
#         #     print(x)
#         # #print(a)
#         # print(s)
#         # print(0/0)
# except:
#     print("ERROR")
#
