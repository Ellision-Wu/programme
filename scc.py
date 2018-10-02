direction={}
rev_dir={}
reached=[]
rev=[]
ano=[]
lens = [] 
out=[]

def MergeSort(array,start,end):
    if start < end -1 :
        mid = (end  -start) // 2 + start
        MergeSort(array,start,mid)
        MergeSort(array,mid,end)
        left = array[start:mid]
        right = array[mid:end]
        i = 0
        j = 0
        for r in range(0,end-start):
            if i==len(left) :
                array[i+j+start] = right[j]
                j += 1
            elif j == len(right):
                array[i+j+start] = left[i]
                i += 1
            elif left[i] <= right[j]:
                array[i+j+start] = left[i]
                i += 1
            else:
                array[i+j+start] = right[j]
                j += 1

for line in open('scc.txt'):
    b=list(line.split())
    try :
        rev_dir[int(b[1])].append(int(b[0]))

    except KeyError: 
        rev_dir[int(b[1])] = [int(b[0])]
    try :
        direction[int(b[0])].append(int(b[1]))
    except KeyError:
        direction[int(b[0])] = [int(b[1])]


def dfs_2(s,dic,visited):
    visited[s]=1
    queue=[]
    vist=[]
    queue.append(s)
    while queue:
        q=queue.pop(0)
        try:
            for i in range(len(dic[q])):
                if visited[dic[q][i]] == 0:
                    visited[dic[q][i]]=1
                    queue.append(dic[q][i])
                    #vist.append(dic[q][i])
            vist.append(q)
        except KeyError:
            pass

    return vist

def dfe_rev_2(s,dic,visited,rev):
    visited[s]=1
    queue=[]
    vist=[]
    queue.append(s)
    while queue:
        q=queue.pop(0)
        vist.append(q)
        id=0
        try:      
            for i in range(len(dic[q])):
                if visited[dic[q][i]] == 0:
                    id=1
                    visited[dic[q][i]]=1
                    queue.append(dic[q][i])
        except KeyError:
            pass
        if id == 0 :
            vist = vist[::-1]
            rev.extend(vist)
            vist=[]
    return rev
keys=list(direction.keys())
maxlen=max(keys)
reached_1=[]
visited=[]
visited_1=[]
visited_2=[]
for i in range(maxlen+3):
    visited.append(0)
    visited_1.append(0)
    visited_2.append(0)


xx=keys[::-1]

rev=[]
for i in range(len(xx)):
    if visited_2[xx[i]] ==0 :
        dfe_rev_2(xx[i],rev_dir,visited_2,rev)


rev=rev[::-1]



for i in range(len(rev)):
    if visited_1[rev[i]]==0:
        rt=dfs_2(rev[i],direction,visited_1)
        ano.extend(rt)
        lens.append(len(ano))


for i in range(len(lens)-1):
    out.append(lens[-i-1]-lens[-i-2])
out.append(lens[0])
MergeSort(out,0,len(out))

print(out[::-1])
'''
def dfs_rev(dic,start,reached,rev):
    reached.append(start)
    id = 1
    try :
        l=len(dic[start])
        for i in range (l):
            if dic[start][i] not in reached:
                id = 0 
                dfs_rev(dic,dic[start][i],reached,rev)
    except KeyError:
        pass
    if id == 1:
        reached=reached[::-1]
        for i in range(len(reached)):
            if reached[i] not in rev:
                rev.append(reached[i])
def dfs(dic,start,reached,i,m):
    if start not in reached:
        reached.append(start)
    if dic[start][i] not in reached:
        dfs(dic,dic[start][i],reached,0,m)
    elif i+1<m:
        dfs(dic,start,reached,i+1,m)

keys=dict.keys(direction)
values=dict.keys(rev_dir)
xx=[]
p=len(direction)
o=0
while o<p:
    o+=1
    if o+1 not in xx and o+1 in keys and o+1 in values:
        txy=len(direction[o+1])
        dfs(direction,o+1,xx,0,txy)
xx=xx[::-1]

for i in range (maxlen):
    if i+1 not in reached_1 and i+1 in keys :
        xs=dfs_2(i+1,direction,visited)
        reached_1.extend(xs)
xx=reached_1[::-1]
print(xx)

for i in range(len(xx)):
    if xx[i] not in reached:
        dfs_rev(rev_dir,xx[i],reached,rev)

print(rev,len(rev))
rev=rev[::-1]

for i in range(len(rev)):
    if rev[i] not in ano:
        fg=len(direction[rev[i]])
        dfs(direction,rev[i],ano,0,fg)
        print(ano)
        lens.append(len(ano))
'''



