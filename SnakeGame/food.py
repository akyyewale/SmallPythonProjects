from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, snakeObj):
        super().__init__()
        self.snakeRef = snakeObj
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-500, 500)
        y = random.randint(-500, 500)
        while self.snakeRef.isOccupied(x, y):
            x = random.randint(-500, 500)
            y = random.randint(-500, 500)
        self.goto(x, y)
