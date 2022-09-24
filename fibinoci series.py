m=int(input("Enter the no. of  terms = "))
x=(input("Enter the positive(1) or negative(0) : "))
n1=0
if(x==1):
	n2=1
else:
	n2=-1
count=0
if(m>1):
	print("fibinoci series upto %d terms= "%m)
	while(count<m):
		print(n1)
		n=n1+n2
		n1=n2
		n2=n
		count+=1
elif(m==1):
	print("fibinoci series upto %d terms = "%m)
	print(n1)
else:
	print("Enter only positive numbers")