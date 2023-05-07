print("Welcome to rollercoaster")
height = int(input("what's you height?"))
age = int(input("What's your age?"))

if height >= 120:
  if age >= 18:
    print("Yoy are good")
  else:
    print("Too young")
else:
  print("Too short")