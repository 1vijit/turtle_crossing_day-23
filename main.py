import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
screen.listen()
screen.onkey(tim.up, "Up")

score = Scoreboard()
score.update_scoreboard()
veh1 = CarManager()
cars = []
cars.append(veh1)
level = 1
count = 0

game_is_on = True
while game_is_on:
    time.sleep(0.3)
    for car in cars:
        car.moves()
    if count+score.level == 15:
        temp = CarManager()
        cars.append(temp)
        count = 0
    else:
        count += 1
    screen.update()

    if tim.ycor() > 250:
        score.level += 1
        score.update_scoreboard()
        tim.reset()
    for car in cars:
        if tim.distance(car)<20:
            score.game_over()
            game_is_on = False
    if score.level >= 15:
        score.win()
        game_is_on = False

screen.exitonclick()
