a=[]
for line in open('as.txt'):
    a.append(int(line[:]))
num=0
print(a[:4])
#2397819673 
#2397819672
def FindInverse(array,start,end):
    global num
    if end - start > 1:
        mid = (end - start) // 2 + start
        FindInverse(array,start,mid)
        FindInverse(array,mid,end)
        left = array[start:mid]
        right = array[mid:end]
        i = 0
        j = 0
        for r in range(0,end-start):
            if i==len(left) :
                array[i+j+start] = right[j]
                num += len(left)-i
                j += 1
            elif j == len(right):
                array[i+j+start] = left[i]
                #num += len(left)-i+1
                i += 1
            elif left[i] <= right[j]:
                array[i+j+start] = left[i]
                #num += len(left)-i+1
                i += 1
            else:
                array[i+j+start] = right[j]
                num += len(left)-i
                j += 1

        return num

print(FindInverse(a,0,len(a)))
