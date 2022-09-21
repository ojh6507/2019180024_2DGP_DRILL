import turtle

def restart():
    turtle.reset()
def forward_move():
    turtle.stamp()
    turtle.forward(50)
def up_move():
    turtle.setheading(90)
    forward_move()    
def right_move():
    turtle.setheading(0)
    forward_move()
def left_move():
    turtle.setheading(180)
    forward_move()
def back_move():
    turtle.setheading(-90)
    forward_move()
    
turtle.shape("turtle")
turtle.onkey(up_move,'W')
turtle.onkey(left_move,'A')
turtle.onkey(back_move,'S')
turtle.onkey(right_move,'D')
turtle.onkey(restart,'Escape')
turtle.listen() 
