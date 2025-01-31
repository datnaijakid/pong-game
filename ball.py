from turtle import Turtle
import random
class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.8, 0.8)
        self.vel_x = 10
        self.vel_y = 10
        
    def move(self):
        self.setx(self.xcor() + self.vel_x)
        self.sety(self.ycor() + self.vel_y)
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.bounce_y()
            
    def bounce_y(self):
        self.vel_y *= -1
        
    def bounce_x(self):
        self.vel_x *= -1
        
    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()
        