lst1=[]
lst2=[]
n1=int(input("Enter number of elements in list1:"))
for i in range(0,n1):
    a=int(input())
    lst1.append(a)
print(lst1)
n2=int(input("Enter number of elements in list2:"))
for i in range(0,n2):
    b=int(input())
    lst2.append(b)
print(lst2)
lst3=lst1+lst2
print("The merged list is:",lst3)
lst3.sort()
print("The merged sorted list is:",lst3)
