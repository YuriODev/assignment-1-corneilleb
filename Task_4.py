# Your solution comes here

positive = 0
negative = 0
zero = 0

for x in range(6):
  num = int(input("enter num: "))
  if num > 0:
    positive += 1
  elif num < 0:
    negative += 1
  else:
    zero += 1

print(f"{positive} {negative} {zero} ")