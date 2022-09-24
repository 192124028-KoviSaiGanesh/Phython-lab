b=input("enter the factorial:")
sum=1
if(b.isnumeric()):
    n=int(b)
    if(n>0):
      for i in range(1,n+1):
        sum=sum*i
      print("the factorial of", n ,"is:",sum)
    else:
       print("invalid")
else:
    print("invalid")
