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

# Main game loop
while True:
    wn.update()
