from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()














































# from turtle import Screen
# from snake import Snake
# from food import Food
# from scoreboard import Scoreboard
# import time
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)    #turns animation on or off
#
# snake = Snake()             #calls the respective function
# food = Food()               #calls the respective function
# scoreboard = Scoreboard()   #calls the respective function
#
# screen.listen()             #listens to the screen
# screen.onkey(snake.up, "Up") #goes up if up arrow is preseed
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")
#
# game_is_on = True
# while game_is_on:
#     screen.update() #Perform a TurtleScreen update.
#     time.sleep(0.1) #Delay execution for a given number of seconds. The argument may be a floating point number for subsecond precision.
#     snake.move()
#
#     #Detect collision with food.
#     if snake.head.distance(food) < 15:  #if distance between head of snake and food <15 most likely for snake to eat
#         food.refresh()            #Refresh the food in a new place
#         snake.extend()            #extend the length of snake
#         scoreboard.increase_score() #increase the score
#
#     #Detect collision with wall.
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         game_is_on=False
#         scoreboard.game_over()
#     #280 is the width of screen, beyond which game will be over
#     #Detect collision with tail.
#     for segment in snake.segments:
#         if segment == snake.head:   #if the segment is the head itself no collision so pass
#             pass
#         elif snake.head.distance(segment) < 10: #if the distance between the head and segment is less than 10 they collide and snake eats itself. Hence game over
#             game_is_on = False
#             scoreboard.game_over()
#
#
#
#
#
# screen.exitonclick()
