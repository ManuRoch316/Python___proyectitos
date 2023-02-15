"""Feliz día"""
import turtle
t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.speed(1)
t.hideturtle()
t.goto(0,-10)

t.pensize(3)
t.color('red')
t.begin_fill()
t.left(140)  
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-140,140)
t.pendown()
t.color('white')
t.write("¿Quieres ser mi Valentin?",font=("Verdana",15,"bold"))

t.penup()
t.goto(-30,90)
t.pendown()
t.color("white")
t.write("@Chema", font=("Verdana",10,"bold"))