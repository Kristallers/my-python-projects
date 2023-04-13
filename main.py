from turtle import *
fönster = Screen()
fönster.bgcolor("blue")
fönster.setup(width=1000, height=600)
fönster.tracer(0)

# vågrätt streck
vs = Turtle()
vs.shape("square")
vs.color("yellow")
vs.shapesize(stretch_wid=5, stretch_len=50)

# lodrätt streck
ls = Turtle()
ls.shape("square")
ls.color("yellow")
ls.shapesize(stretch_wid=50, stretch_len=5)
ls.penup()
ls.goto(-200,0)

# huvudloop
while True:
    fönster.update()

