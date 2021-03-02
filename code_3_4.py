print("Welcome to BMI calculator")
height = float(input("what's is your height in m? "))
weight = float(input("what's is your weight in kg? "))

bmi = weight / (height ** 2)

if bmi < 18.5:
   print(f"your bmi is  {bmi}, yor are under weight")
elif bmi < 25:
     print(f"your bmi is {bmi},you  are in normal weight")
elif bmi < 30:
     print(f"your bmi is  {bmi},you are slightly over weight")
elif bmi < 35:
     print(f"your bmi is  {bmi},you are obese")
else:
  print(f"your  bmi is {bmi},you are clinically obese")
