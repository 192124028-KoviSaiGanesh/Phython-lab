
def word(str1, str2, m, n):
 
    if m == 0:
        return n
 
    if n == 0:
        return m
 
    if str1[m-1] == str2[n-1]:
        return word(str1, str2, m-1, n-1)
 
    return 1 + min(word(str1, str2, m, n-1),    
                   word(str1, str2, m-1, n),    
                   word(str1, str2, m-1, n-1)    
                   )
 
str1 =input("Enter Your String1 : ")
str2 = input("Enter Your String : ")
print (word(str1, str2, len(str1), len(str2)))
