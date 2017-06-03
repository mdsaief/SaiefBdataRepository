import turtle

def drawSquare():

    window = turtle.Screen()
    window.bgcolor("black")

  
    sqr = turtle.Turtle()
    sqr.shape("circle")
    sqr.color("white")
    sqr.speed(3)
    
    sqr.forward(100)
    sqr.right(90)
    sqr.forward(100)
    sqr.right(90)
    sqr.forward(100)
    sqr.right(90)
    sqr.forward(100)
    sqr.right(90)

    sqr2 = turtle.Turtle()
    sqr2.shape("arrow")
    sqr2.color("red")
    sqr2.circle(100)

    window.exitonclick()

drawSquare()
