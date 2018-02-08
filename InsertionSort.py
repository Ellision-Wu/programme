def InsertionSort(array,start,end):
    for j in range(start+1,end):
        key = array[j]
        i = j-1
        while i >= 0 and array[i]>key:
            array[i+1]=array[i]
            i-=1
        array[i+1]=key
a = [1,2,3,45,23,56,1243,8,32]
InsertionSort(a,0,len(a))
print(a)