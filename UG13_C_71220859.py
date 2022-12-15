import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor('blue')

#huruf T
t.penup()
t.goto(-300,200)
t.pendown()
t.forward(100)
t.back(50)
t.right(90)
t.forward(100)

t.forward(100)
t.penup()

#angka 5
t.goto(-100,100)
t.pendown()
t.left(180)
t.forward(100)
t.right(90)
t.forward(100)
t.back(100)
t.goto(-100,100)
t.forward(100)
t.right(90)
t.pendown()
t.forward(100)
t.right(90)
t.forward(100)

#huruf P
t.penup()
t.goto(100,100)
t.pendown()
t.left(90)
t.forward(100)
t.right(180)
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)


#angka 9
t.penup()
t.goto(-100,0)


















s.exitonclick()
