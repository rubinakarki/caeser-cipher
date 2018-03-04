import turtle
def box(argument):
	argument.right(75)
	argument.forward(100)
	argument.right(45)		
	argument.forward(100)
	argument.right(135)
	argument.forward(100)
	argument.right(45)
	argument.forward(100)


def square():

	window=turtle.Screen()
	window.bgcolor('blue')
	window.title('what is this?')

	brad = turtle.Turtle()
	brad.color('yellow')
	brad.shape('classic')
	brad.speed(100)
	for i in range(1,80):
		box(brad)
		brad.right(5)

	window.exitonclick()#lslslslsl
	
square()
