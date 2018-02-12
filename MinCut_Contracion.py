import random,copy
###########WORING!!!!!!!WRONG!!!!!!!!!!!###########
###########WORING!!!!!!!WRONG!!!!!!!!!!!###########
###########WORING!!!!!!!WRONG!!!!!!!!!!!###########
###########WORING!!!!!!!WRONG!!!!!!!!!!!###########
###########WORING!!!!!!!WRONG!!!!!!!!!!!###########
###########WORING!!!!!!!WRONG!!!!!!!!!!!###########
###########WORING!!!!!!!WRONG!!!!!!!!!!!###########
###########WORING!!!!!!!WRONG!!!!!!!!!!!###########
###########WORING!!!!!!!WRONG!!!!!!!!!!!###########
###########WORING!!!!!!!WRONG!!!!!!!!!!!###########
###########WORING!!!!!!!WRONG!!!!!!!!!!!###########

a=[]
for line in open('4444.txt'):
    a.append(str.split(line[:]))
count=0


def MinCut_Contracion(lis):
    while len(lis) > 2:
        col=len(lis)
        nod1 = random.randint(0,col-1)
        nod2 = random.randint(0,col-1)
        if nod1 == nod2:
            MinCut_Contracion(lis)
        else:
            for i in range(len(lis[nod2])):
                lis[nod1].append(lis[nod2][i])
            del lis[nod2]
            MinCut_Contracion(lis)
    return lis

def MinCut_Find(ori,conted):
    num1=[]
    leen=len(conted[0])-1
    cut=0
    count=0
    while count < leen:
        num1.append(int(conted[0][count]))
        count += len(ori[num1[-1]-1])
    for i in range(len(conted[1])):
        if int(conted[1][i])  in num1:
            cut +=1
    print(num1)
    return cut


dic={}
c=copy.deepcopy(a)

for i in range(0,1):
    MinCut_Contracion(a)
    print(a)
    tim = MinCut_Find(c,a)
    if tim in dic:
        dic[tim] += 1
    else  :
        dic[tim] = 1 
    a = copy.deepcopy(c)
minum = min(dict.keys(dic))
print(minum)