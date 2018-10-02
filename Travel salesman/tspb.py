import matplotlib.pyplot as plt
import math
x=[]
y=[]
for line in open ('tspb.txt'):
    a=str.split(line[:])
    if len(a)==1:
        al=int(a[0])
    else:
        x.append(float(a[1]))
        y.append(float(a[2]))


clu=["inf" for i in range(al)]

clu[0]=0
net=0
sta=0
le=9999999
pas=0
indica=0
while indica != al-1: 
    for i in range(al):
        if clu[i]=='inf':
            dis=math.sqrt((x[i]-x[sta])*(x[i]-x[sta]) + (y[i]-y[sta])*(y[i]-y[sta]))
            if dis < le:
                le=dis
                net=i
        else:
            pass

    indica +=1
    clu[net]=le
    sta=net
    pas+=le
    le=99999999
    print(sta,indica)
print(pas+math.sqrt((x[0]-x[sta])*(x[0]-x[sta]) + (y[0]-y[sta])*(y[0]-y[sta])))
