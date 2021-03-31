from turtle import Screen
import time
from snake import Snake
from food import Food
from pen import Pen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

colors = ["red","green","blue", "pink","orange", "Dark Red", "AliceBlue","cyan","brown", "azure"]

my_snake = Snake()
screen.listen()
screen.onkey(my_snake.move_right, "Right")
screen.onkey(my_snake.move_left, "Left")
screen.onkey(my_snake.move_up, "Up")
screen.onkey(my_snake.move_down, "Down")
# todo: add element to tail, triggered by scheduler

move_on = True
food_dot = Food()
pen = Pen()
score = 0

while move_on:
    pen.update_score(score)
    move_on = my_snake.move()
    if my_snake.head.distance(food_dot) < 15:
        food_dot.new_food()
        score += 1
        pen.update_score(score)
    screen.update()
    time.sleep(0.2)

screen.exitonclick()







