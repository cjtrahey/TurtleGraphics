# Pre-written code
import turtle               #import the turtle library

# Definitions
seymour = turtle.Turtle()   #create a turtle object, name the turtle seymour 
seymour.showturtle()        #show the turtle object
seymour.shape("turtle")     #make the shape of the object a turtle

# The Square
seymour.forward(300)
seymour.right(90)
seymour.forward(300)
seymour.right(90)
seymour.forward(300)
seymour.right(90)
seymour.forward(300)


# The "Cross"
seymour.right(90)
seymour.forward(150)
seymour.right(90)
seymour.forward(300)
seymour.right(270) # A Spin for Style! Could also use `seymour.left(90)` here instead.
seymour.forward(150)
seymour.right(270)
seymour.forward(150)
seymour.left(90)
seymour.forward(300)
seymour.right(720) # He's celebrating! (Also used for viewer to get a chance to view object)