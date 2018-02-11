array=[1,2,3,45,6,7,8,9,34,453,345,23,56,1234,12]

start=0
end=len(array)


tab={array[start]:start,array[end-1]:end-1,array[(end-start-1)//2+start]:(end-start-1)//2+start}
box=[array[start],array[end-1],array[(end-start-1)//2+start]]
box.remove(min(box))
box.remove(max(box))
comp=tab[box.pop(0)]
print(array,comp,start,end,tab)
