import turtle
import tkinter
import time
import random

def run_game():
    delay = 0.1
    score = 0
    high_score = 0

    #Creating the window for the game
    wn = turtle.Screen()
    turtle.TurtleScreen._RUNNING=True
    wn.title('Snake Game')
    wn.bgcolor('black')

    #Setting the width & height of the screen...can be edited by user
    wn.setup(width=800, height=800)
    wn.tracer(0)

    #Creating the initial one block (head) of the 'snake'
    head = turtle.Turtle()
    head.shape('square')
    head.color('white')
    head.penup()
    head.goto(0,0) #Center of the screen
    head.direction = 'Stop'

    #Creating the 'food' for the snake to eat within the game.
    food = turtle.Turtle()
    food.color('red')
    food.speed(0)
    food.shape('circle')
    food.penup()
    food.goto(0,100)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape('square')
    pen.color('white')
    pen.penup()
    pen.hideturtle()
    pen.goto(0,250)



    #Assigning keyboard values to move/control the snake
    def go_up():
        if head.direction != 'down':
            head.direction = 'up'

    def go_down():
        if head.direction != 'up':
            head.direction = 'down'

    def go_left():
        if head.direction != 'right':
            head.direction = 'left'

    def go_right():
        if head.direction != 'left':
            head.direction = 'right'

    # Assigning movment buttons
    def move():
        if head.direction == 'up':
            y = head.ycor()
            head.sety(y+20)
        if head.direction == 'down':
            y = head.ycor()
            head.sety(y-20)
        if head.direction == 'left':
            x = head.xcor()
            head.setx(x-20)
        if head.direction == 'right':
            x = head.xcor()
            head.setx(x+20)


    wn.listen() #Listening to user selections in order
    wn.onkeypress(go_up, 'w')
    wn.onkeypress(go_down, 's')
    wn.onkeypress(go_left, 'a')
    wn.onkeypress(go_right, 'd')


    segments = []

    gamePlay = True
    #Block for main gameplay (snake grows, the food is 'eaten' and so forth).
    while gamePlay:
        wn.update()
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1) #End the game if the snake hits a wall
            gamePlay = False
            wn.reset()
            turtle.Screen().bye() #Close the Turtle screen window
            
        if head.distance(food) < 20:
            x = random.randint(-270,270)
            y = random.randint(-270,270)
            food.goto(x,y)

            # Adding new blocks to snake
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("orange")  # tail color
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 10
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write(f"Score: {score} High Score: {high_score}", align="center", font=('candara', 18,'bold'))
            # Checking for head collisions with body segments
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        move()
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                gamePlay = False
                head.goto(0, 0)
                head.direction = "stop"
                for segment in segments:
                    segment.goto(1000, 1000)
                segment.clear()
                score = 0
                delay = 0.1
                pen.clear()
                pen.write(f"Score: {score} High Score: {high_score}", align="center", font=('candara', 18,'bold'))
        time.sleep(delay)




