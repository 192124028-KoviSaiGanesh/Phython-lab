a=input("enter the number:")
x=0
y=1
sum=0
if(a.isnumeric()):
    n=int(a)
    if(n<=0):
       print("invalid")
    else:
       for i in range(0,n):
         print(sum,end=' ')
         x=y
         y=sum
         sum=x+y
else:
    print("invalid")
