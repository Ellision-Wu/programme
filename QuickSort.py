

def Sort(array,start,end):
    mid = start
    for i in range (start,end-1):
        if array[i] < array[end-1]:
            ex = array[mid]
            array[mid] = array[i]
            array[i] = ex
            mid += 1
    ex2 = array[mid]
    array[mid] = array[end-1]
    array[end-1] = ex2
    return mid

def QuickSort(array,start,end):
    if start < end-1:
        separ = Sort(array,start,end)
        QuickSort(array,start,separ)
        QuickSort(array,separ+1,end)
    else:
        pass
a = [1,4,2,0,-1,6,54,3,7,12,4,6,58,9,234,43546,2,5,76,78,2,45,7,6,-32,-2,3-4,5,3]
QuickSort(a,0,len(a))
print(a)