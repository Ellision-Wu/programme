a=[]
b=[]


for line in open('a.txt'):
    a=(str.split(line[:]))

    if len(a)==2:
        total = [int(a[0]),int(a[1])]
        vis=[]
        lis=[]
        for i in range(total[0]+1):
            vis.append(0)
            lis.append([])
    else:
        fi=int(a[0])
        se=int(a[1])
        tr=int(a[2])
        lis[fi].append((se,tr))
        lis[se].append((fi,tr))
cost=0
o=1
po=[1]
count=1
wit=[]
while(count<=499):
    vis[o]=1
    
    for i in range(len(lis[o])):
        wit.append(lis[o][i])
    mi=wit[0][0]
    val=wit[0][1]
    for i in range(len(wit)):
        if wit[i][1]<val and vis[wit[i][0]]!=1:
            mi=wit[i][0]
            val=wit[i][1]
    o=mi
    cost+=val
    po.append(o)
    count+=1

print(po,cost)

###  111  69119377652
###  222  67311454237

###  333   -3612829

