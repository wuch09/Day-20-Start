from turtle import Turtle, Screen
#from main import colors
import random

element_colors = ["red","green","blue", "pink","orange", "Dark Red", "AliceBlue","cyan","brown", "azure"]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]
        self.length = 3

    def create_snake(self):
        for _ in range(3):
            new_tx = Turtle("square")
            new_tx.color(random.choice(element_colors))
            new_tx.penup()
            new_tx.goto(int(-20 * _), 0)
            new_tx.speed("slowest")
            self.snake_list.append(new_tx)

    def head_position(self):
        return self.head.position()

    def is_hit_food(self, loc):
        if self.head_position() == loc:
            return True
        else:
            return False

    def move(self):

        good_move = True

        for index in range(self.length-1, 0, -1):
            self.snake_list[index].goto(self.snake_list[index-1].position())
        self.head.forward(MOVE_DISTANCE)

        for index in range(1, self.length):
            if self.head.distance(self.snake_list[index]) < 15:
                good_move = False

        if abs(self.head_position()[0]) >= 280 or abs(self.head_position()[1]) >= 280:
            good_move = False

        return good_move


    def add_element_to_tail(self):
        print("add_element")
        self.length += 1
        new_element = Turtle("square")
        new_element.color(random.choice(element_colors))
        new_element.penup()
        new_element.speed("slowest")
        length = len(self.snake_list)
        new_element.goto(self.snake_list[length-1].position())
        self.snake_list.append(new_element)


    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

