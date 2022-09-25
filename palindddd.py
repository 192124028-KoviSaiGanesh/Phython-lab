def first_letter_index(str, left, right):
   index = -1
   for i in range(left, right + 1):
      if str[i] >= 'a' and str[i] <= 'z' :
         index = i
         break
   return index
def last_letter_index(str, left, right):
   index = -1
   for i in range(left, right - 1, -1) :
      if str[i] >= 'a' and str[i] <= 'z':
         index = i
         break
   return index
def solve(str):
   left = 0
   right = len(str) - 1
   flag = True
   for i in range(len(str)) :
      left = first_letter_index(str, left, right)
      right = last_letter_index(str, right, left)
      if right < 0 or left < 0:
         break
      if str[left] == str[right]:
         left += 1
         right -= 1
         continue
      flag = False
      break
   return flag
s = input("enter string:")
print(solve(s))
