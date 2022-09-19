from turtle import Turtle
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
   def __init__(self):
      super().__init__()
      self.color("black")
      self.penup()
      self.hideturtle()
      self.level = 0
      self.update_scoreboard()

   def update_scoreboard(self):
      self.clear()
      self.goto(-250, 250)
      self.write(arg=f"Level= {self.level}", move=False, align="left", font=FONT)

   def game_over(self):
      self.goto(0,0)
      self.color("red")
      self.write(arg="GAME OVER", move=False, align="center", font=FONT)

   def win(self) :
      self.goto(0, 0)
      self.color("red")
      self.write(arg="YOU WIN!", move=False, align="center", font=FONT)