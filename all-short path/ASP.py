for line in open('g3.txt'):
    a=str.split(line[:],' ')
    if len(a)==2:
        all=int(a[0])
        b=[['inf' for i in range(0,all+1)] for i in range(all+1)]
        for i in range(all+1):
            b[i][0]=[]
        
    else:
        b[int(a[0])][int(a[1])]=int(a[2])
        b[int(a[0])][0].append(int(a[1]))
#Bellman-ford
bell=[0 for i in range(all+1)]
for i in range(all):
    for j in range(all+1):
        for k in b[j][0]:
            old = bell[k]
            new = bell[j]+b[j][k]
            if new < old :
                bell[k]=new

for j in range(all):
    for k in b[j][0]:
        old = bell[k]
        new = bell[j]+b[j][k]
        if new < old :
            print("error")


print(bell)

for i in range(all+1):
    for j in b[i][0]:
        b[i][j]=b[i][j]+bell[i]-bell[j]
res=[[]]
for i in range(all):
    rou=['inf' for l in range(all+1)]
    rou[i+1]=0
    rea=[]
    notr=[i+1]
    for j in notr :
        if j not in rea:
            rea.append(j)
            for k in b[j][0]:
                notr.append(k)
                if rou[k]=='inf':
                    rou[k]=b[j][k]+rou[j]
                elif rou[j]+b[j][k]< rou[k]:
                    rou[k]=rou[j]+b[j][k]
                    notr.append(k)
                    try :
                        rea.remove(k) 
                    except ValueError:
                        pass

    res.append(rou)
re=[]
for i in range(len(res)):
    for j in range(len(res[i])):
        if res[i][j]=='inf':
            pass
        else:
            res[i][j]=res[i][j]-bell[i]+bell[j]
            re.append(res[i][j])

print(min(re))