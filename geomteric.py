import turtle  				#standard library
def	 geometric_shapes():	 		
	window=turtle.Screen()	#setting screen to displey geomteric figures
	window.bgcolor('yellow')
	move = turtle.Turtle()	#creating the instance to access class Turtle
	move.color('red')
	move.speed(3)
	move.shape('circle')
	move.shapesize(1,2)
	i=0					 	 #making square
	while i<4:
		move.forward(100)
		move.right(90)
		i +=1
	
	lol=turtle.Turtle() 	#making circle
	lol.shape('turtle')
	lol.color('black')
	lol.circle(120)
	
	newinstance=turtle.Turtle()	#making triangle
	newinstance.shape('triangle')
	newinstance.color('blue')
	i=0
	while i<3:
		newinstance.forward(100)
		newinstance.left(120)
		i +=1

	rec =turtle.Turtle()	#rectangle
	rec.shape('classic')
	rec.shapesize(2,2)
	rec.forward(100)
	rec.left(90)
	rec.forward(20)
	rec.left(90)
	rec.forward(100)
	rec.left(90)
	rec.forward(20)
	rec.left(90)

	window.exitonclick()

geometric_shapes()