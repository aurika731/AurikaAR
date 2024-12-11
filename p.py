import turtle


screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor('aquamarine')

t = turtle.Turtle()
t.hideturtle()
t2 = turtle.Turtle()

t2.hideturtle()
t2.penup()

t2.penup()



t.penup()
t.goto(0, 50)
t.pendown()
t.write("Can you hit it?", font=("Arial", 24, "bold"), align="center")
t.penup()
t.goto( 0, -50)
t.pendown()
t.write("Cornbread Maxwell", font=("Arial", 24, "bold"), align="center")

turtle.addshape('tteok.gif' )
t2.shape("tteok.gif")
t2.goto(-200,200)
a = t2.stamp()
t2.goto(200,200)


turtle.addshape('tteokbokki.gif' )
t2.shape("tteokbokki.gif")
t2.goto(200,-200)
a = t2.stamp()
t2.goto(200,-200)


enter = input("Press Enter to Continue")


screen.bgcolor('purple')

t.clear()
t2.clear()
t2.clearstamps()
t.write("page2", font=("Arial", 24, "bold"), align="center")



turtle.done()




turtle.addshape('archery.gif')
t2.shape("archery.gif ")
t2.goto(200,200)
a = t2.stamp()
t2.goto(200,200)

turtle.addshape("baking.gif")
t2.shape("baking.gif")
t2.goto(200,200)
a = t2.stamp()
t2.goto(200,200)

enter = input("Press Enter to Continue")


screen.bgcolor('yellow')

t.clear()
t2.clear()
t2.clearstamps()
t.write("page3", font=("Arial", 24, "bold"), align="center")




turtle.addshape('snow white.gif')
t2.shape("snow white")
t2.goto(200,200)
a = t2.stamp()
t2.goto(200,200)


turtle.addshape('harry potter.gif')
t2.shape("harry potter.gif")
t2.goto(200,200)
a = t2.stamp()
t2.goto(200,200)

enter = input("Press Enter to Continue")


screen.bgcolor('pink')

t.clear()
t2.clear()
t2.clearstamps()
t.write("page4", font=("Arial", 24, "bold"), align="center")



turtle.addshape('fashion.gif')
t2.shape("fashion.gif")
t2.goto(200,200)
a = t2.stamp()
t2.goto(200,200)

turtle.addshape('Volleyball.gif')
t2.shape("Volleyball gif")
t2.goto(200,200)
a = t2.stamp()
t2.goto(200,200)