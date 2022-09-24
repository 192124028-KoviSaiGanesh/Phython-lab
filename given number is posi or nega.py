x=input("number:")
if(x.isnumeric()) or ((x.startswith("-"))):
    a=int(x)
    if(a>0):
        print("positive")
    else:
       print("negative")
else:
     print("invalid")
