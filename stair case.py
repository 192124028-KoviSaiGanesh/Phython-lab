def way(n):
    if n <= 1:
        return n
    return way(n-1) + way(n-2)
 
def countWays(s):
    return way(s + 1)
 

s = int(input("Enter Input : "))
print("Number of ways = ",countWays(s))
