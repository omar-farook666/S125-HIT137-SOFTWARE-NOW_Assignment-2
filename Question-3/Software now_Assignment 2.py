import turtle

def tree(moveLength, turtle, depth):
    if depth > 0:
        turtle.forward(moveLength)
        turtle.color("green")
        
        # Branch to the right
        turtle.right(25)
        tree(moveLength * 0.7, turtle, depth - 1)
        
        # Return to original position and branch to the left
        turtle.left(50)
        tree(moveLength * 0.7, turtle, depth - 1)
        
        # Return to the main branch
        turtle.right(25)
        
        turtle.penup()
        turtle.backward(moveLength)
        turtle.pendown()

def main():
    # Set up the turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    myTurtle = turtle.Turtle()
    myTurtle.left(90)  # Start pointing upwards
    myTurtle.speed(0)
    
    # Start the tree with a length of 100 and a depth of 5
    tree(100, myTurtle, 5)
    
    turtle.done()

if __name__ == "__main__":
    main()
