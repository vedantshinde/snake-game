from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.penup()
        self.color("Yellow")
        self.display_score()
        self.hideturtle()

    def update_score(self, factor=1):
        self.score += factor

    def display_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def display_text(self, text,game_over=False):
        self.goto(0,0)
        self.write(text, align=ALIGNMENT, font=FONT)
        if not game_over:
            time.sleep(0.5)
            self.display_score()
