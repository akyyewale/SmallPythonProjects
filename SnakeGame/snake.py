import turtle


class Snake:
    snake = []

    def __init__(self, length):
        for index in range(length):
            tim = turtle.Turtle("square")
            tim.color("white")
            tim.penup()
            tim.setposition(-20 * index, 0)
            self.snake.append(tim)
        self.head = self.snake[0]

    def update(self):
        for segNum in range(len(self.snake) - 1, 0, -1):
            self.snake[segNum].goto(self.snake[segNum - 1].xcor(), self.snake[segNum - 1].ycor())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def isOccupied(self, x, y):
        for seq in self.snake:
            if seq.distance(x, y) < 15:
                return True
        return False

    def addSeg(self):
        tim = turtle.Turtle("square")
        tim.color("white")
        tim.penup()
        lastseg = self.snake[len(self.snake)-1]
        tim.setposition(lastseg.xcor(), lastseg.ycor())
        self.snake.append(tim)
