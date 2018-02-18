direction={}
rev_dir={}
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
    b=(str.split(line[:]))
    try :
        rev_dir[int(b[1])].append(int(b[0]))
    except KeyError:
        rev_dir[int(b[1])] = [int(b[0])]
    try :
        direction[int(b[0])].append(int(b[1]))
    except KeyError:
        direction[int(b[0])] = [int(b[1])]



reached=[]
rev=[]

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
ano=[]

def dfs(dic,start,reached):
    reached.append(start)
    try:
        x = dic[start]
        for i in range (len(x)):
            print(i,end='')
            if x[i] not in reached:
                dfs(dic,x[i],reached)
    except KeyError:
        pass
    except RuntimeError :
        pass

xx=[]
for i in range(len(direction)):
    if i+1 not in xx:
        print(i+1,end='')
        dfs(direction,i+1,xx)
xx=xx[::-1]
'''
for i in range(len(xx)):
    if xx[i] not in reached:
        dfs_rev(rev_dir,xx[i],reached,rev)
rev=rev[::-1]

lens = [] 

for i in range(len(rev)):
    if rev[i] not in ano:
        dfs(direction,rev[i],ano)
        lens.append(len(ano))
out=[]

for i in range(len(lens)-1):
    out.append(lens[-i-1]-lens[-i-2])
out.append(lens[0])
MergeSort(out,0,len(out))
out=out[::-1]'''
print(xx)


