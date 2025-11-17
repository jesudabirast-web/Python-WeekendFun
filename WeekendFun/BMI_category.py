weight = int(input('Enter the weight in kg: '))
height = int(input('Enter the height in meters: '))

BMI = weight / (height * height)

if(BMI < 18.5):
	print("Your BMI is Underweight")

if(BMI > 18.5 and BMI < 24.9):
	print("Your BMI is Normal")

if(BMI >= 25 and BMI < 29.9):
	print("Your BMI is Overweight")  

if(BMI >= 30):
	print("Your BMI is Obese")

