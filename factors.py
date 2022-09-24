a=input("enter the factor:")
count=0
if(a.isnumeric()):
    n=int(a)
    if(n>=0):
      for i in range(1,n+1):
       if(n%i==0):
        count=count+1
        print(i)
      print("number of factors:",count)
    else:
      print("invalid")
else:
    print("invalid")
