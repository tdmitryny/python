height = float(input("What is your height in meters?"))
weight = float(input("What is your weight in kg:?"))

bmi = int(weight) / float(height) * 2

if bmi <= 18:
    print(f"Your BMI {bmi * 100}, you are in shape")
elif bmi >= 18.5:
    if bmi < 25:
      print(f"Your BMI {bmi}, you have normal weight")
elif bmi > 25:
    if bmi < 30:
      print(f"Your BMI {bmi}, you are overweight")
elif bmi > 30:
    if bmi < 35:
      print(f"Your BMI {bmi}, you are obese") 
elif bmi > 35:
    print(f"Your BMI {bmi}, clinical obese")   
    
