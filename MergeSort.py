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

                
a = [1,-2,4,0,2,4,5,7,3,6,78,9,456,3,87,456,82,12,0,434,0.345,2134]
MergeSort(a,0,len(a))
print(a)

