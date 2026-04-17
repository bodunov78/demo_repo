from re import *
for i in range(0,10**9,23):
    # reg=rf"(12345[0-9]7)*)"
    pattern = r'[^12]\d{1,3}7\d8$'
    # reg = rf'(?=({reg}))'
    if match(pattern, str(i)):
        print (i)