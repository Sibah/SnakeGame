import turtle
from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Siba's Python Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
# If head collides with food
    if snake.head.distance(food) < 20:
        print("That's delicious")
        food.move()
        score.increaseScore()
        snake.extend_snake()

# If head hits the wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score.gameOver()
        game_on = False

# Detect if the head hits the snake tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.gameOver()

screen.exitonclick()