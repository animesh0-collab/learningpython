#Pattern Printing Problems
#Problem 1

#Printing Stars '*' in Right Angle Triangle Shape
num = int(input())
for i in range(1,num+1):
  for j in range(1,i+1):
      print("*",end=" ")
  print()


#Problem 2
num = int(input())
for i in range(num):
   stars = 2*i + 1
   print("*" * stars)


#Printing Stars '*' in Pyramid Shape

num = int(input())
for i in range(num):
   spaces = " " * (num -i-1)
   stars = "* " * (i+1)
   print(spaces + stars)

#Revesr Version of the above Pyramid Shape
num = int(input())
for i in range(num):
   spaces = " "  * i
   stars = "* " * (num-i)
   print(spaces + stars)

# Hollow Triangle 
n = int(input())

for row in range(n):
    if row == 0:
        print(" " * (n - 1) + "*")
    elif row == n - 1:
        print("*" * n)
    else:
        leading = " " * (n - row - 1)
        middle = " " * (row - 1)
        print(leading + "*" + middle + "*")