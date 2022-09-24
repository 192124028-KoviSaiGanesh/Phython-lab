name=input("enter the name:")
register=int(input("enter the register:"))
print("enter the 5 subjects marks:")
a=input()
s=input()
d=input()
f=input()
g=input()
if(a.isnumeric() and s.isnumeric() and d.isnumeric() and f.isnumeric() and g.isnumeric()):
    m1=int(a)
    m2=int(s)
    m3=int(d)
    m4=int(f)
    m5=int(g)
    total=m1+m2+m3+m4+m5
    avg=total/500*100
    print("enter the name:",name)
    print("enter the register:",register)
    print("enter marks:",m1)
    print("enter marks:",m2)
    print("enter marks:",m3)
    print("enter marks:",m4)
    print("enter marks:",m5)
    print("total:",total)
    print("avg:",avg)
    if(avg>=80 and avg<=100):
            print("grade A")
    elif(avg>=60 and avg<80):
         print("grade B")
    elif(avg>=40 and avg<60):
          print("grade C")
    else:
       print("fail")
else:
    print("invalid")
