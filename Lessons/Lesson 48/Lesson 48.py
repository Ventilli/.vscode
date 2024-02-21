import turtle 

turtle1 = turtle.Turtle()
turtle1.shape('turtle')
turtle1.pensize(6)



def romb():
    turtle1.color('yellow')

    turtle1.begin_fill()

    turtle1.pencolor('orange')
    turtle1.right(45)
    turtle1.forward(80)

    turtle1.pencolor('cyan')
    turtle1.left(90)
    turtle1.forward(80)

    turtle1.pencolor('green')
    turtle1.left(90)
    turtle1.forward(80)

    turtle1.pencolor('violet')
    turtle1.left(90)
    turtle1.forward(80)

    turtle1.end_fill()

    turtle.exitonclick()

turtle1.penup()
turtle1.goto(-300, -20)
    
turtle1.pendown()
turtle1.left(170)
turtle1.circle(50, 210)

turtle1.penup()
turtle1.goto(-250, -120)

turtle1.pendown()
turtle1.goto(-210, -20)
turtle1.goto(-170, -120)
turtle1.goto(-190, -70)
turtle1.goto(-230, -70)

turtle1.penup()
turtle1.goto(-120, -120)

turtle1.pendown()
turtle1.goto(-90, -20)
turtle1.goto(-70, -120)
turtle1.goto(-50, -20)
turtle1.goto(-30, -120)

turtle1.penup()
turtle1.goto(-10, -120)

turtle1.pendown()
turtle1.goto(-10, -20)
turtle1.goto(-10, -120)
turtle1.goto(30, -20)
turtle1.goto(30, -120)

turtle.done()


# turtle1.pencolor('white')
# turtle.bgcolor('black')

# turtle1.penup()
# turtle1.goto(0, -100)
# turtle1.pendown()
# turtle1.circle(100)
# turtle1.penup()
# turtle1.home()
# turtle1.dot(50, 'green')

# turtle1.goto(0, 50)
# turtle1.home()
# turtle1.goto(40, 20)
# turtle1.home()
# turtle1.goto(-40, 20)
# turtle1.home()
# turtle1.goto(0, -50)
# turtle1.home()
# turtle1.goto(-40, -20)
# turtle1.home()
# turtle1.goto(40, -20)
# turtle1.home()

# i = 0
# turtle1.right(45)
# turtle1.forward(60)
# while i != 3:
#     turtle1.left(90)
#     turtle1.forward(60)
#     i += 1

# for i in range(10, 0, -1):
#     turtle1.shapesize(i, i, i)
#     turtle1.forward(30)

turtle.exitonclick()
