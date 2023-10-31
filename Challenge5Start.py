# Pre-written code

import turtle               # Import the turtle library

seymour = turtle.Turtle()   # Create a turtle object, name the turtle seymour
seymour.showturtle()        # Show the turtle object
seymour.shape("turtle")     # Make the shape of the object a turtle

seymour.pensize(8)
seymour.pencolor("black")

# Draw an envelope

# Create the rectangle

seymour.forward(300)
seymour.right(90)
seymour.forward(200)        
seymour.right(90)           
seymour.forward(300)        
seymour.right(90)           
seymour.forward(200)        
seymour.right(90)           

# Create the flaps

seymour.goto(150, -100) 
seymour.goto(300, 0)
seymour.right(720) # He's celebrating! (Also used for viewer to get a chance to view object)