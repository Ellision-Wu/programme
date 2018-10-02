a=[]
b=[]
c=[]
for line in open('mwis.txt'):
    a.append(int(line))
le=a[0]
a=a[1:]


for i in range(le+2):
    b.append(0)
    c.append([])
b[0]=0
b[1]=a[0]
c[0].append(0)
c[1].append(1)
for i in range(len(a)):
    if i==0:
        pass
    else:
        if b[i]>=b[i-1]+a[i]:
            mx=b[i]
            c[i+1]=c[i]

        else :
            mx=b[i-1]+a[i]

            c[i+1]=c[i+1]+c[i-1]
            c[i+1].append(i+1)

        #mx=max(b[i],b[i-1]+a[i])
        b[i+1]=mx
b=b[1:-1]

print(c[-2])