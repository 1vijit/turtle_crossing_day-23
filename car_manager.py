from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.color(random.choice(COLORS))
        self.shape("square")
        self.tiltangle(0)
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(x= 250-STARTING_MOVE_DISTANCE,y=random.randrange(-300, 300))
        self.moves()
    def moves(self):
        self.forward(MOVE_INCREMENT)
