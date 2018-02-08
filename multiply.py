
a=1234454533
b=5234452333
ans=0
print(len(str(a)))


def Multiply(num1,num2):
    num1=str(num1)
    num2=str(num2)
    if len(num1)<=1 or len(num2)<=1:
        return int(num1)*int(num2)
    else:
        num11=int(num1[:len(num1)//2]) 
        num12=int(num1[len(num1)//2:])
        num21=int(num2[:len(num2)//2])
        num22=int(num2[len(num2)//2:])  
        num3= num11*num21
        num4=num12*num22
        num5=(num12+num11)*(num22+num21)-num3-num4
        ans=10**(2*len(str(num12)))*num3+num5*10**(len(str(num12)))+num4
        return int(ans)

ans=Multiply(a,b)

if ans == a*b:
    print(ans,a*b)
    print("True")
else:
    print(ans,a*b)
    print("False")