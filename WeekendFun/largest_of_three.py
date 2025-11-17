input_one = int(input('Enter an integer: '))
input_two = int(input('Enter a second integer: '))
input_three = int(input('Enter a third integer: '))

largest_number = input_one

if(input_one > input_two and largest_number):
	largest_number = input_two

if(input_three > input_two and largest_number):

print("The largest number is", largest_number)