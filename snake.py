from turtle import Turtle
import time

SEG_DELTA = 20
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self, screen, num_segments=3):
        self.snake = []
        self.screen = screen

        self.create_snake(self.snake, num_segments)
        self.head = self.snake[0]

        self.key_bindings()

    def add_segment(self, x_cor, y_cor):
        s = Turtle(shape="square")
        s.penup()
        s.goto(x_cor, y_cor)
        s.color("white")
        self.snake.append(s)

    def create_snake(self, snake, num_segments):
        x_pos = 0
        for _ in range(num_segments):
            self.add_segment(x_pos, 0)
            x_pos -= SEG_DELTA

    def extend_snake(self):
        self.add_segment(self.snake[-1].xcor(), self.snake[-1].ycor())


    def key_bindings(self):
        self.screen.listen()

        self.screen.onkey(self.turn_up, "Up")
        self.screen.onkey(self.turn_down, "Down")
        self.screen.onkey(self.turn_left, "Left")
        self.screen.onkey(self.turn_right, "Right")

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self, sleep_time=0.1):
        self.screen.update()
        time.sleep(sleep_time)

        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)



