import turtle

#method to move forward with an angle
def turnAndMove(manoj, length, angle):
	manoj.forward(length)
	manoj.right(angle)

#method to create a new instance of a Tutle with shape, color and speed
def getATurtleWith(shape, color, speed):
	new = turtle.Turtle()
	new.shape(shape)
	new.color(color)
	new.speed(speed)
	return new

#function to create a square shape
def draw_square(manoj, length):
	
	for index in range(4):
		turnAndMove(manoj, length, 90)

	return manoj

	#draw a circle
	#angie = getATurtleWith("arrow", "yellow", 5)
	#angie.circle(length)

	#draw a Triangle
	#triangle = getATurtleWith("turtle", "red", 5)
	#for index in range(3):
		#turnAndMove(triangle, length, 120)

def draw_circle_from_square():

	window = turtle.Screen()
	window.bgcolor("white")

	#draw a square
	manoj = getATurtleWith("turtle", "pink", 5)

	for index in range(36):
		square = draw_square(manoj, 100)
		square.right(10)

	window.exitonclick()

draw_circle_from_square()
