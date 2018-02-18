a=[]
b=[[]]
dic={}
for line in open('a.txt'):
    a=(str.split(line[:]))
    c=[]
    for i in range(len(a)):
        if i == 0 :
            pass
        else:
            d=str.split(a[i],',')
            c.append((int(d[0]),int(d[1])))
    b.append(c)

unreached=[]
reached=[]
for i in range(0,201):
    unreached.append(10000)
unreached[1]=0
term=[]
def dij(node, reached,unreached,lis,term):
    if node not in reached :
        reached.append(node)
    start = unreached[node]
    link = lis[node]
    nex={}
    for i in range(len(link)):
        end = link[i][0]
        weight = link[i][1]+start
        nex[weight] = end
        if weight < unreached[end]:
            unreached[end]=weight

    ke =min(dict.keys(nex))
    while nex[ke]  in reached:
        nex.pop(ke)
        if not nex :
            break
        ke=min(dict.keys(nex))

    if  nex:
        dij(nex[ke], reached,unreached,lis,term)
    else :
        term.append(node)
        for i in range(len(reached)):
            if reached[-1-i] not in term:
                dij(reached[-1-i], reached,unreached,lis,term)
                break

dij(1,reached,unreached,b,term)

print(term)


