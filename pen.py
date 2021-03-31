from turtle import Turtle


class Pen(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_score(self, score):
        self.goto(50, 280)
        self.clear()
        self.write("Your Score : "+str(score), font=("Arial", 10, "normal"))

