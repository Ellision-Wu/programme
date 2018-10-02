a=[]
for line in open('4.txt'):
    a.append(int(line[:]))
count=0


#start
def Sort_start(array,start,end):
    global count
    mid = start+1
    count += (end-start-1)
    for i in range (start,end):
        if array[i] < array[start]:
            ex = array[mid]
            array[mid] = array[i]
            array[i] = ex
            mid += 1
    ex2 = array[mid-1]
    array[mid-1] = array[start]
    array[start]= ex2
    return mid-1



def QuickSort(array,start,end):
    if start < end-1:
        tab={array[start]:start,array[end-1]:end-1,array[(end-start-1)//2+start]:(end-start-1)//2+start}
        box=[array[start],array[end-1],array[(end-start-1)//2+start]]
        box.remove(min(box))
        box.remove(max(box))
        comp=tab[box.pop(0)]
        if comp == start:
            separ = Sort_start(array,start,end)
        elif comp == end:
            ex2 = array[start]
            array[start] = array[end-1]
            array[end-1]= ex2
            separ = Sort_start(array,start,end)

        else:
            ex2 = array[start]
            array[start] = array[comp]
            array[comp]= ex2
            separ = Sort_start(array,start,end)
        QuickSort(array,start,separ)
        QuickSort(array,separ+1,end)
        return
    else:
        pass
print(a)
QuickSort(a,0,len(a))
#print(a)
print(a,count)