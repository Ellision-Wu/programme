import matplotlib.pyplot as plt
import math
x=[]
y=[]
for line in open ('tsp.txt'):
    a=str.split(line[:])
    if len(a)==1:
        pass
    else:
        x.append(float(a[0]))
        y.append(float(a[1]))

x=x[11:13]
y=y[11:13]
print(14662.0046407879+14409.202165641733-1314.2382487374398*2)
mat=[]
for i in range(len(x)):
    start=[x[i],y[i]]
    d=[]
    for j in  range(len(x)):
        end=[x[j],y[j]]
        dis=math.sqrt((end[0]-start[0])*(end[0]-start[0]) + (end[1]-start[1])*(end[1]-start[1]))
        d.append(dis)
    mat.append(d)

dic={}
al=len(x)
print(mat)
plt.scatter(x,y)
plt.show(1)

'''for i in range(al):
    vis=[q for q in range(al)]
    vis.remove(i)
    for j in range(al):
        if j in vis:
            dic[2**i+2**j]=mat[i][j]
            vis.remove(j)
'''
plt.scatter(x,y)
plt.show(1)

print(len(x))

ext=[]
for i in range(al):
    dic[(i,0)]=mat[i][0]
for j in range(2,2**al)  :
    if j % 2 ==1:
        continue
    else: 

        for i in range(al):
            dic[(i,j)]=9999999999999999

            if ((2**i)&(j))!=0 :
                continue
            else:
                for k in range(al):
                    if ((2**k)&j) != 0 :
                        if dic[(i,j)] >= mat[i][k] + dic[(k,j-(2**k))]:
                            dic[(i,j)] = mat[i][k] + dic[(k,j-(2**k))]

print(dic,dic[0,j-1])
a=(1,2)

