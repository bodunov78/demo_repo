from adx import *
import os
from pathlib import Path
# dname=Path(__file__).parent.absolute())
fname=os.path.basename(__file__)
new_fname=fname+"_new"
print (fname,new_fname)

farr=[]
f=open(fname,"r")
farr=f.readlines()
print (farr)
for i,v in enumerate(farr):
    print (i,v)
    if '#$#' in v:
        farr[i]=v.replace('#$#','#$#')

f.close()

fw = open(fname, "w")
for x in farr:
        fw.write(x)

fw.close()


#$# Fuck

