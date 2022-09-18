import turtle
import random
def restart():
    turtle.reset()
    
def forward_move():
    turtle.forward(50)
    turtle.stamp()
def right_move():
    turtle.right(90)
    forward_move()
def left_move():
    turtle.left(90)
    forward_move()
def back_move():
    turtle.left(180)
    forward_move()
    
turtle.shape("turtle")
turtle.onkey(forward_move,'W')
turtle.onkey(left_move,'A')
turtle.onkey(back_move,'S')
turtle.onkey(right_move,'D')
turtle.onkey(restart,'Escape')
turtle.listen() 
