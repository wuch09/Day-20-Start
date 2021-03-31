from turtle import Turtle
import random
xy_size = 620


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.penup()
        self.goto(random.randrange(-200, 200, 40), random.randrange(-200, 200, 40))

    def new_food(self):
        new_xcor = random.randrange(-200, 200, 20)
        new_ycor = random.randrange(-200, 200, 20)
        # print(f"xcor :{new_xcor}, ycor : {new_ycor}")
        self.goto(new_xcor, new_ycor)














