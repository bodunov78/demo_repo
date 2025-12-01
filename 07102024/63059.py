import string
import re
# print('Ха-ха!?'.rstrip(string.punctuation))  # 'Ха-ха'
with open("pn.txt") as f:
    cnt=0
    for x in f:
        x=x.replace('-',' ')
        a = list(x.split())
        for s in a:
            if re.findall(r'\b\w{4}\b', s):
                cnt+=1
                print(s)
        # x=x.rstrip(',.?!:",')
        # x = x.rstrip(string.punctuation)

        # x=x.replace('-',' ')
            # .replace(',',' ').replace(';',' ').replace('!',' ').replace('?',' ')
#         a=list(x.split())
#         for s in a:
#             if len(s)==4:
#                 cnt+=1
#                 print(s)
print(cnt)