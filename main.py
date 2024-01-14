#Turtle Party Project
#By Alecia Stanley
#1.14.24

import turtle
turtle.color("red")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.right(360 / num)

polygon(4, 100)
Back (125)
polygon(3, 50)
