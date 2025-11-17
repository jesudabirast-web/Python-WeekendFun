total_bill = input("Enter the total bill amount: ")
is_member = input("Are you a member, yes or no: ")

if(total_bill >= 1000 and is_member == yes):
	print("You get 10% off your purchase")

if(total_bill >= 1000 and is_member != yes):
	print("You get 5% off your purchase")

if(total_bill < 1000 and is_member != yes):
	print("Your total is $", total_bill, "Buy 3 get 1 free off your next purchase")
