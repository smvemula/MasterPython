import turtle

#method to move forward with an angle
def turnAndMove(manoj, length, angle):
	manoj.right(angle)
	manoj.forward(length)

def draw_m(manoj):
	turnAndMove(manoj, 100, 270)
	turnAndMove(manoj, 100, 150)
	turnAndMove(manoj, 100, 240)
	turnAndMove(manoj, 100, 150)

def draw_v(manoj):
	turnAndMove(manoj, 100, 240)
	turnAndMove(manoj, 100, 180)
	turnAndMove(manoj, 100, 240)

def draw_k(manoj):
	turnAndMove(manoj, 100, 270)
	turnAndMove(manoj, 50, 180)
	manoj.left(120)
	manoj.forward(100)
	turnAndMove(manoj, 100, 180)
	turnAndMove(manoj, 100, 240)

def draw_manoj_initials():

	window = turtle.Screen()
	window.bgcolor("white")

	new = turtle.Turtle()
	new.shape("turtle")
	new.color("white")
	new.speed(5)

	new.backward(300)

	new.color("blue")
	draw_m(new)

 	new.color("white")
 	new.left(90)
	new.forward(100)

	new.color("blue")
	draw_v(new)

	new.color("white")
 	new.right(150)
	new.forward(100)
	new.left(90)
	new.forward(100)

	new.color("blue")
	draw_m(new)

	new.color("white")
 	new.left(90)
	new.forward(100)

	new.color("blue")
	draw_k(new)

	window.exitonclick()

draw_manoj_initials()