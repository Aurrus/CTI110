#import and setting vals
import turtle
wn = turtle.Screen()
wn.bgcolor("light blue")      
wn.title("P4LAB1")      

t = turtle.Turtle()
t.color("green")           
t.pensize(3)               
#triangle
for i in [0,1,2]:
    t.forward(100)
    t.left(120)

t.penup()
t.forward(150)
t.pendown()

#square
for i in [0,1,2,3]:
    t.forward(50)
    t.left(90)

wn.mainloop()
