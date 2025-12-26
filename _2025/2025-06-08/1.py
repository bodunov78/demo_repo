# from sys import *
# from math import *
# from functools import *
# from itertools import *
# from turtle import *
# from fnmatch import *
# # 1 76216
#
# t="12,16,23,24,26,27,28,37,45,47,58,68"
# g="ЕГ,ЕВ,ВГ,ВА,АГ,ГБ,ГД,ГИ,БД,ДИ,ИЖ,ЖЕ"
# t=t+','+t[::-1]
# g=g+','+g[::-1]
#
# s="АБВГДЕЖИ"
#
# for ss in permutations(s):
#     nt=g
#     for i,v in enumerate(ss):
#         nt=nt.replace(v,str(i+1))
#     if set(nt.split(','))==set(t.split(',')):
#         print (ss)
#
#
#
# # 2 69907
#
# t="13,18,25,28,34,36,46,57,67,78"
# g="DE,EA,EB,AH,HC,HG,CF,FG,GB,BD"
# t=t+','+t[::-1]
# g=g+','+g[::-1]
#
# s="ABCDEFGH"
#
# for ss in permutations(s):
#     nt=g
#     for i,v in enumerate(ss):
#         nt=nt.replace(v,str(i+1))
#     if set(nt.split(','))==set(t.split(',')):
#         print (ss)