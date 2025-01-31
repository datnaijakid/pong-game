from turtle import Turtle
VEL = 20

class Characters(Turtle):

    def __init__(self):
        super().__init__()
        self.right = (370, 0)
        self.left = (-370, 0)

    def create_char(self, position):
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.goto(position)

    def char_left(self):
        self.create_char(self.left)

    def char_right(self):
        self.create_char(self.right)

    def move_up(self, HEIGHT):
        if self.ycor() <= HEIGHT/2 - 70:
            self.sety(self.ycor() + VEL)

    def move_down(self, HEIGHT):
        if self.ycor() >= -HEIGHT/2 + 70:
            self.sety(self.ycor() - VEL)

    def draw_center(self, HEIGHT):
        center = Turtle()
        center.hideturtle()
        center.speed("fastest")
        center.shape("square")
        center.penup()
        center.color("white")
        center.goto(10, HEIGHT / 2)
        center.right(90)
        for _ in range(int(HEIGHT / 40)):
            center.forward(20)
            center.penup()
            center.forward(20)
            center.pendown()
