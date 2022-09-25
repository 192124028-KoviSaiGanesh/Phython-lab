n=int(input("Enter Your Year : "))
if(n>0):
   if(n%400==0):
    print("Your Year is a Leap Year")
   elif((n%4==0)and (n%100!=0)):
    print("Your Year is a Leap Year")
   else:
    print("Your Year is not a Leap Year")
else:
    print("Invalid Year")
