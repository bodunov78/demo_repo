s="1?2711*0"

from fnmatch import *

for x in range (0, 10**10+1, 4891):
    if fnmatch(str(x),'1?2711*0'):
        print(x)