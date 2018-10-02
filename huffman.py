import MergeSort
a=[]
for line in open('ksbig.txt'):
    lin=line.split()
    a.append([int(lin[0]),int(lin[1])])
size=a[0]
a=[[0,0]]+a[1:]
lis=[]

for i in range(2):
    b=[]
    for x in range(size[0]+1):
        b.append(0)
    lis.append(b)
    print(i)
exi=0

wei=size[0]

while exi<=size[1]:
    i=exi%2
    if i==0:
        for o in range(len(lis[0])):
            if exi==0 or o==0:
                lis[0][o]=0
            v= o-a[exi][1]
            if v <0:
                lis[0][o]=lis[1][o]
            else:
                v1=lis[1][o]
                v2=lis[1][v]+a[exi][0]
                lis[0][o]=max(v1,v2)
    elif i==1:
        for o in range(len(lis[1])):
            if exi==0 or o==0:
                lis[1][o]=0
            v= o-a[exi][1]
            if v <0:
                lis[1][o]=lis[0][o]
            else:
                v1=lis[0][o]
                v2=lis[0][v]+a[exi][0]
                lis[1][o]=max(v1,v2)
    print(exi)
    exi+=1
print(lis[0][-1],lis[1][-1])

'''    for o in range(len(lis[i])):
        if i==0 or o==0:
            lis[i][o]=0
        v= o-a[i][1]
        if v <0:
            lis[i][o]=lis[i-1][o]
        else:
            v1=lis[i-1][o]
            v2=lis[i-1][v]+a[i][0]
            lis[i][o]=max(v1,v2)'''
#2493893   4243395