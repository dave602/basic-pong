# Basic Pong Game
# By David A
# July 2020

import turtle
import os

# Game Window
window = turtle.Screen()
window.title("Pong by David A")
window.bgcolor("black")
window.setup(width=1024, height=600)
window.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-462, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(462, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .3
ball.dy = .3

# Score Tracker
p1_score = 0
p2_score = 0

# Default Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: %d        Player 2: %d" % (p1_score, p2_score), align="center", font=("courier", 24, "normal"))


# Function
def paddle_a_up():
    y_cord = paddle_a.ycor()
    y_cord += 20
    paddle_a.sety(y_cord)

def paddle_a_down():
    y_cord = paddle_a.ycor()
    y_cord -= 20
    paddle_a.sety(y_cord)


def paddle_b_up():
    y_cord = paddle_b.ycor()
    y_cord += 20
    paddle_b.sety(y_cord)

def paddle_b_down():
    y_cord = paddle_b.ycor()
    y_cord -= 20
    paddle_b.sety(y_cord)


# Key Binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop

while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1



    if ball.xcor() > 502:
        ball.goto(0, 0)
        ball.dx *= -1
        p1_score += 1
        pen.clear()
        pen.write("Player 1: %d        Player 2: %d" % (p1_score, p2_score), align="center",
                  font=("courier", 24, "normal"))

    if ball.xcor() < -502:
        ball.goto(0, 0)
        ball.dx *= -1
        p2_score += 1
        pen.clear()
        pen.write("Player 1: %d        Player 2: %d" % (p1_score, p2_score), align="center",
                  font=("courier", 24, "normal"))

    # Paddle and ball collision
    if (ball.xcor() > 452 and ball.xcor() < 462) and (ball.ycor() < paddle_b.ycor() + 55 and ball.ycor() > paddle_b.ycor() -55):
        ball.setx(452)
        ball.dx *= -1
        os.system("aplay bounce.wav&")
    if (ball.xcor() < -452 and ball.xcor() > -462) and (ball.ycor() < paddle_a.ycor() + 55 and ball.ycor() > paddle_a.ycor() -55):
        ball.setx(-452)
        ball.dx *= -1
        os.system("aplay bounce.wav&")


