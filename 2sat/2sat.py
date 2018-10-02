import random 
d=[]
for line in open('2sat1.txt'):
    a=str.split(line[:],' ')
    if len(a)==1:
        al=int(a[0])
        b=['inf' for i in range(0,al+1)]
        
    else:
        d.append([int(a[0]),int(a[1])])
ind=1
for o in range(al):
    for o in range(al):
        for i in range(al):
            c=[]
            for j in range(al):
                c.append(random.randint(0,1))
            ind3=0
            for k in range(len(d)):
                ind2=0
                a1=d[k][0]
                a2=d[k][1]
                #print(a1,a2)
                if a1<0 and c[(-a1)-1]==0:
                    #print(a1,c,(-a1)-1)
                    ind2=1
                elif a1>0 and c[a1-1]==1:
                    ind2=1
                    #print(a1,c,(a1)-1)
                if a2<0 and c[(-a2)-1]==0:
                    ind2=1
                    #print(a2,c,(-a2)-1)
                elif a2>0 and c[a2-1]==1:
                    ind2=1
                    #print(a2,c,(a2)-1)
                if ind2==1:
                    ind3+=1
                else:
                    break
            if ind3==len(d):
                print(c)
                exit(0)
            else:
                print(i)

print('no')

#[0, 1, 1, 1, 1, 1, 1, 0, 1, 1,d1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0]
#[1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0]





