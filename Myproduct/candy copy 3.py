from turtle import *

circle(100)

for i in range(4):
    up()
    left(90)
    forward(20)
    right(90)
    down()

    circle(80-i*20)

up()
left(90)
forward(20)
right(90)
down()


circle(100, 60)

for i in range(17):
    begin_fill()
    up()
    setpos(0, 100)
    right(40)
    down()
    
    circle(100, 60)