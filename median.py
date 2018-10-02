
big=[]
small=[]
sm=0
bi=0
count=0
med=0
for line in open('Median.txt'):
    count+=1
    b=int(line)
    if b >= bi :
        big.append(b)
        bi = min(big)
    else:
        small.append(b)
        sm=max(small)
    if len(big)-len(small)>=2:
        big.remove(bi)
        small.append(bi)
        sm=bi
        bi = min(big)
    elif len(small)-len(big )>=2 :
        small.remove(sm)
        big.append(sm)
        bi=sm
        sm=max(small)
    if count%2:
        if len(big)>len(small):
            med+=bi
        else: 
            med+=sm
    else:
        med+=sm

print(med%10000,med)