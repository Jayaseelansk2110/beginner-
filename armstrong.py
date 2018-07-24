a=int(input("enter the number "))
b=a
sum=0
while(b!=0):
    rem=b%10
    sum=sum+(rem**3)
    b//=10
if(sum==a):
    print("armstrong")
else:
    print("not armstrong")
