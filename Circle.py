# a circle is drawn using squares
import turtle
import random

def draw_square():
    # random colors
    col = ["red","white","blue","yellow","green"]
    window = turtle.Screen()
    
    # setting the window background to black
    window.bgcolor("black")

    pp = turtle.Turtle()
    pp.shape("arrow")
    pp.color("white")
    pp.speed(0)

    for k in range(360):            #loop to turn the square
        for i in range(4):          #to make a simple square
            pp.forward(100)         #forward step
            pp.right(90)            #to make a turn
            pp.color(random.choice(col))        #changing the color of every line drawn
        pp.right(1)                 #the degrees the square will turn

    window.exitonclick()

draw_square()
