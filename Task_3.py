# Your solution comes here

num = int(input('Enter 3 digit integer: '))

a = num//100
b = (num //10) % 10
c = num % 10



if a==b==c:
  print(3)
elif (a==b  or a==c or b==c):
  print(2)
else:
  print(0)
  
