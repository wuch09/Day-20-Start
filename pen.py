from turtle import Turtle


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
        self.write("Your Score : "+str(self.score), font=("Arial", 10, "normal"))

