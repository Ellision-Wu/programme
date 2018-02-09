
a=3141592653589793238462643383279502884197169399375105820974944592
b=2718281828459045235360287471352662497757247093699959574966967627
ans=0

def Multiply(num1,num2):
    num1=str(num1)
    num2=str(num2)
    num11=int(num1[:len(num1)//2]) 
    num12=int(num1[len(num1)//2:])
    num21=int(num2[:len(num2)//2])
    num22=int(num2[len(num2)//2:])  
    num3= num11*num21
    num4=num12*num22
    num5=(num12+num11)*(num22+num21)-num3-num4
    ans=10**(2*len(str(num11)))*num3+num5*10**(len(str(num11)))+num4
    return int(ans)

ans=Multiply(a,b)

if ans == a*b:
    print(ans,a*b)
    print("True")
else:
    print(ans,a*b)
    print("False")