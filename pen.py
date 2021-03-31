from turtle import Turtle

FONT = ("Arial", 12, "normal")
GAME_OVER_FONT = ("Arial", 24, "normal")
class Pen(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_score(self):
        self.goto(-50, 280)
        self.clear()
        self.write("Your Score : "+str(self.score), font=FONT)

    def game_over(self):
        self.goto(-200, 0)
        self.write("Game Over ! Your Score : " + str(self.score), font=GAME_OVER_FONT)

    def increase_score(self):
        self.score += 1


