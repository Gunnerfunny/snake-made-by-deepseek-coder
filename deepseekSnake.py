import turtle
import time
import random

# set up screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # turns off the screen updates to speed things up

# snake head
head = turtle.Turtle()
head.speed(0)  # animation speed
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)  # start at the center of the screen
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-290, 290), random.randint(-290, 290))

# snake body (as a list of turtles)
segments = []

# score
score = 0
score_turtle = turtle.Turtle()
score_turtle.speed(0)
score_turtle.color("white")
score_turtle.penup()
score_turtle.goto(-290, 260)
score_turtle.write("Score: {}".format(score), align="left", font=("Arial", 14, "normal"))
score_turtle.hideturtle()

# function to move the snake forward one segment at a time
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# bind keys to functions
wn.listen()
wn.onkeypress(go_up, "W")
wn.onkeypress(go_down, "S")
wn.onkeypress(go_left, "A")
wn.onkeypress(go_right, "D")

# main game loop
while True:
    wn.update()  # updates the screen

    # move the snake forward one segment at a time
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    # check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        
        # add a new segment to the body and increase score
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        score += 10
        score_turtle.clear()  # clear the old score
        score_turtle.write("Score: {}".format(score), align="left", font=("Arial", 14, "normal"))

    # check for collision with wall
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)  # pause the game
        head.goto(0, 0)  # reset snake to center
        head.direction = "stop"
        
        # hide all segments of body
        for segment in segments:
            segment.goto(2000, 2000)  # move the segments off screen
            
        # clear the list of segments
        segments = []

        # reset score to zero
        score = 0
        score_turtle.clear()
        score_turtle.write("Score: {}".format(score), align="left", font=("Arial", 14, "normal"))
