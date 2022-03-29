import turtle
import snake
import time
import food

screen = turtle.Screen()
screen.setup(1000, 1000)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = snake.Snake(5)
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(snake.down, "s")

food = food.Food(snake)
screen.update()

isGameOver = False
while not isGameOver:
    screen.update()
    time.sleep(0.1)
    snake.update()
    if snake.head.distance(food.xcor(),food.ycor()) < 15 :
        food.refresh()
        snake.addSeg()


screen.exitonclick()