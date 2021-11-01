from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

# ----------
# Screen setup
# ----------

screen = Screen()
screen.title(titlestring="Snake Game")
screen.bgcolor("black")
screen.screensize(canvwidth=600, canvheight=600)
screen.setup(width=610, height=610, startx=None, starty=None)
screen.tracer(n=0)

# ------------
# Create Borders
# -------------
border = Turtle()
border.goto(-300, 300)
border.hideturtle()
border.color("red")
border.speed("fastest")
border.width(20)
for _ in range(4):
    border.forward(600)
    border.right(90)

# ------------
# Create Snake & Food
# -------------
snake = Snake(screen=screen)
food = Food()
scoreboard = Scoreboard()

# -------------
# Move the snake
# --------------
game_is_on = True
SLEEP_TIME = 0.1


def hit_the_wall(x_cor, y_cor):
    if x_cor >= 300 or x_cor <= -300 or y_cor >= 300 or y_cor <= - 300:
        return True
    else:
        return False


while game_is_on:
    snake.move(sleep_time=SLEEP_TIME)

    # Detect Collision With the food
    if snake.head.distance(food) < 17:
        snake.extend_snake()
        food.relocate()
        scoreboard.update_score()
        scoreboard.display_score()

        # Increase speed/Level:
        if scoreboard.score % 2 == 0 and SLEEP_TIME > 0.02:
            SLEEP_TIME -= 0.02
            scoreboard.display_text(text="⬆️SNAKE SPEED ⬆️")

    # Detect collision with wall
    if hit_the_wall(snake.head.xcor(), snake.head.ycor()):
        game_is_on = False
        scoreboard.display_text(text="Game Over! \nYou Hit a wall!", game_over=True)

    # Detect collision with self
    for seg in snake.snake[1:]:
        if seg.distance(snake.head) < 10:
            game_is_on = False
            scoreboard.display_text(text="Game Over! \nYou Bit Yourself!", game_over=True)

screen.exitonclick()
