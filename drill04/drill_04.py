import turtle

count = 4
HorizonCount = 4
turtle.penup()
turtle.goto(-500,500)
turtle.pendown()
VerticalCount = 5
y = 500
while VerticalCount > 0:
    while HorizonCount > 0:
        while count > 0:
            turtle.forward(100)
            turtle.right(90)
            count-=1

        turtle.forward(100)
        count =4
        while count > 0:
            turtle.forward(100)
            turtle.right(90)
            count-=1
        HorizonCount-=1
    
    y-=100
    turtle.penup()
    turtle.goto(-500,y)
    turtle.pendown()
    count =4
    VerticalCount -=1
    HorizonCount = 4
   
    
   

