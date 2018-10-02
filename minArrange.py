a=[]
b=[]


for line in open('a.txt'):
    a=(str.split(line[:]))

    if len(a)==1:
        total = int(a[0])
    else:
        
        c=[int(a[0])-int(a[1]),int(a[0]),int(a[1])]
        b.append(c)


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
            elif left[i][0] <= right[j][0]:
                array[i+j+start]= left[i]
                i += 1
            else:
                array[i+j+start] = right[j]
                j += 1

def MergeSort_2(array,start,end):
    if start < end -1 :
        mid = (end  -start) // 2 + start
        MergeSort_2(array,start,mid)
        MergeSort_2(array,mid,end)
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
            elif left[i][1] <= right[j][1]:
                array[i+j+start]= left[i]
                i += 1
            else:
                array[i+j+start] = right[j]
                j += 1
MergeSort(b,0,len(b))
stop=0
#print(b)

for i in range(len(b)):
    if b[i][0]!=b[i-1][0]:
        MergeSort_2(b,stop,i)
        stop=i

b=b[::-1]
print(b)
time=0
sum=0
for i in range (len(b)):

    sum += b[i][1]*(b[i][2]+time) 
    time=b[i][2]+time
print(sum)

###  111  69119377652
###  222  67311454237



