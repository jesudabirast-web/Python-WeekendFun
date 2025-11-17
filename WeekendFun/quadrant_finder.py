x = int(input("Enter first integer for x: "))
y = int(input("Enter second integer for y: "))

if(x > 0 & y < 0 ):
	print("Quadrant 1")

if(x < 0 & y > 0):
	print("Quadrant 2")

if(x < 0 & y < 0):
	print("quadrant 3")

if(x > 0 & y < 0):
	print("quadrant 4")

if(x == 0 & y == 0):
	print("Origin")

if(y == 0 & x != 0):
	print("X-axis")

if(x == 0 & y != 0):
	print("Y-axis")
