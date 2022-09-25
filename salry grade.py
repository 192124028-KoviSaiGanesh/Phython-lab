g=input("Enter the Employee Grade : ")
s=int(input("Enter the Employee Salary : "))
print("Salary = ", s)
if(s<0):
    print("Invalid Salary ")
else:
    if(g=='A'):
        bonus=0.05*s
        print("Bonus= ", bonus)
    elif(g=='B'):
        bonus=0.1*s
        print("Bonus= ", bonus)
    else:
        print("Enter Valid Grade")
    
    if(s<10000):
         eg=0.02*s
         tb=eg+bonus
         print("Total Bonus With Extra Bonus = ", tb)
         total=tb+s
   
    else:
         total=bonus+s

    print("Total to be paid : ",total)

