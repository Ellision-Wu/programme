a=[]
b=[]
d=[]
c=[]
import math
vis=[]
for line in open('big.txt'):
    a=(str.split(line[:]))

    if len(a)==2:
        total = int(a[0])
    else:
        l=0
        for i in range(len(a)) :
            if a[i]=='1':
                l+=2**i
        c.append(l)
for i in range(total):
    vis.append(-1)
group=[]
mer=[]
print(vis)
test=[]
for i in range(len(c)) :
    test.append([])
    for u in range(i-1,len(vis)) :
        o=c[i]^c[u] 
        test[i].append(o)
    if i==1000:
        print(2)
print(test)
'''    for u in vis:
        o=c[i]^c[u]
        if o==0:
            b.append([i+1,u+1,o])
        else:
            lo=math.log(o,2)
            if len(str(lo))==3 and lo<=3:
                b.append([i+1,u+1,lo])
    del vis[0]'''








#106
