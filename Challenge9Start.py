# Pre-written Code
import turtle               #import the turtle library

seymour = turtle.Turtle()   #create a turtle object, name the turtle seymour 
seymour.showturtle()        #show the turtle object
seymour.shape("turtle")     #make the shape of the object a turtle

seymour.pensize(4)

# Octagon & Color Fill
seymour.color("red")
seymour.begin_fill()
for i in range(3):
    seymour.forward(75)
    seymour.right(45)
    seymour.forward(75) #draws octagon and fills it red
    seymour.right(45)
    seymour.forward(75)
    seymour.right(45)
seymour.end_fill()

# write STOP on the octagon
seymour.color('white')
seymour.penup()
seymour.goto(-20,-110) #lines up Seymour to draw 'stop'
seymour.pendown()
seymour.write('STOP', font=('Verdana', 40, 'bold'))

# place seymour off to the side of the drawing
seymour.penup()
seymour.goto(0, 20)
seymour.pendown()
seymour.right(720) # He's celebrating! (Also used for viewer to get a chance to view object)





