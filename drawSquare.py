import turtle

def drawSquare():

    window = turtle.Screen()
    window.bgcolor("red")

  
    sqr = turtle.Turtle()
    sqr.shape("turtle")
    
    sqr.forward(100)
    sqr.right(90)
    sqr.forward(100)
    sqr.right(90)
    sqr.forward(100)
    sqr.right(90)
    sqr.forward(100)
    sqr.right(90)

    window.exitonclick()

drawSquare()
