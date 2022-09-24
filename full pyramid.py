n=input("Enter number of rows:")
if(n.isnumeric()):
    rows=int(n)
    for i in range(0,rows):
      for j in range(1,(rows-i)+1):
         print('', end='') 
      for j in range(0,i+1):
         print(j+1,end=' ')
      print()
else:
    print("invalid")
