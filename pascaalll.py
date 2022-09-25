from math import factorial
r=int(input("Enter The Number of Rows:"))
for i in range(r):
        for j in range(r-i+1):
                print(end=" ")
        for j in range(i+1):
                print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        print()
