R=6371

for H in range(0,12):
    L=((R+H)**2 -R**2)**0.5
    print (H,L)