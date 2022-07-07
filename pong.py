# Pong game
# By @ntonio

import turtle

wn = turtle.Screen()
wn.title("Pong by @ntonio")
wn.bgcolor("black")
wn.setup(height=600, width=800)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # the speed of animation set to maximum, not the speed of the paddle
paddle_a.shape("square")  # measures of the default turtle square are 20px wide by 20px high
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # Disables the line by default in all turtles
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # the speed of animation set to maximum, not the speed of the paddle
paddle_b.shape("square")  # measures of the default turtle square are 20px wide by 20px high
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()  # Disables the line by default in all turtles
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # the speed of animation set to maximum, not the speed of the paddle
ball.shape("square")  # measures of the default turtle square are 20px wide by 20px high
ball.color("white")
ball.penup()  # Disables the line by default in all turtles
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1



# Movement Functions
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


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:  # si la bola toca el borde superior
        ball.sety(290)  # la vuelvo a poner en el borde
        ball.dy *= -1  # cambio el signo (sentido) a la direccion de la bola

    if ball.ycor() < -290:  # si la bola toca el borde inferior
        ball.sety(-290)  # la vuelvo a poner en el borde
        ball.dy *= -1  # cambio el signo (sentido) a la direccion de la bola

    if ball.xcor() > 390:  # si la bola toca el borde izq
        ball.goto(0, 0)  # la vuelvo a poner en el centro
        ball.dx *= -1  # cambio el signo (sentido) a la direccion de la bola

    if ball.xcor() < -390:  # si la bola toca el borde derecho
        ball.goto(0, 0)  # la vuelvo a poner en el centro
        ball.dx *= -1  # cambio el signo (sentido) a la direccion de la bola

        # Paddle and Ball Collisions Right Paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1  # cambio el signo (sentido) a la direccion de la bola

        # Paddle and Ball Collisions Left Paddle
    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1  # cambio el signo (sentido) a la direccion de la bola

