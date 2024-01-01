from turtle import Turtle
import random
class Food(Turtle):     #turtle is a super class and as it is called everything from turtle class can be used here

    def __init__(self):
        super().__init__()
        self.shape("circle")        #shape of food is circle
        self.penup()                #do not draw anything
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)    #if food is found stretches itself
        self.color("blue")          #color of food
        self.speed("fastest")       #speed
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)    #if food is spotted refresh x cor
        random_y = random.randint(-280, 280)    #refresh y cor
        self.goto(random_x, random_y)   #moves food to new cor
