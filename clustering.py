a=[]
b=[]
d=[]
c=[]
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
            elif left[i][2] <= right[j][2]:
                array[i+j+start]= left[i]
                i += 1
            else:
                array[i+j+start] = right[j]
                j += 1


for line in open('1.txt'):
    a=(str.split(line[:]))

    if len(a)==1:
        total = int(a[0])
    else:
        b.append( [int(a[0]), int(a[1]),int(a[2])])

for i in range(total+1) :
    c.append(1)
    d.append([i])
print(d)
MergeSort(b,0,len(b))
x=0

while len(d)>4  :
    fis=b[x][0]
    sec=b[x][1]

    for v in range(len(d)):
        for t in d[v]:
            if t==fis :
                fisc=v
    for v in range(len(d)):
        for t in d[v]:
            if t==sec :
                secc=v
    if secc != fisc :
        d[fisc]=d[fisc]+d[secc]
        del d[secc]
    x+=1
print(b[x-1])
#106
