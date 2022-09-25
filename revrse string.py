def reverse(str):
    string = " "
    for i in str:
        string = i + string
    return string
str = input("Enter Your String : ")
print("The original string is:",str)
print("The reverse string is:", reverse(str)) 
