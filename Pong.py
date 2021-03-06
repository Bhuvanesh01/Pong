# Classic Pong Game made using Python and turtule Module

import turtle
import winsound

win = turtle.Screen()
win.title("Pong by Bhuvanesh")
win.setup(width=800, height=600)
win.bgpic("Background.png")
win.tracer(0)

# Score
score_a = 0
score_b = 0
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)  

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0) 

# Ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = 0.3 

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 230)
pen.write(" 0 ", align="Left", font=("Courier", 44, "normal"))
pen.write(" 0 ", align="Right", font=("Courier", 44, "normal"))


# Paddle Movement Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard Binding
win.listen()
win.onkeypress(paddle_a_up,"w")  
win.onkeypress(paddle_a_down,"s")  
win.onkeypress(paddle_b_up,"Up")  
win.onkeypress(paddle_b_down,"Down")  

# Main Game Loop
while True:
    win.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(" {} ".format(score_b), align="Left", font=("Courier", 44, "normal"))
        pen.write(" {} ".format(score_a), align="Right", font=("Courier", 44, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(" {} ".format(score_b), align="Left", font=("Courier", 44, "normal"))
        pen.write(" {} ".format(score_a), align="Right", font=("Courier", 44, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # AI Player
    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_up()
    elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_down()
    if score_a == 10 :
        win.clear()
        win.bgcolor("Black")
        pen.clear()
        pen.goto(0,0)
        pen.write("Player A Wins!!!", align = "Center", font=("Courier", 44, "normal"))
        win.ontimer(win.bye,1000)
    elif score_b == 10 :
        win.clear()
        win.bgcolor("Black")
        pen.clear()
        pen.goto(0,0) 
        pen.write("Player B Wins!!!", align = "Center", font=("Courier", 44, "normal"))
        win.ontimer(win.bye,1000)
