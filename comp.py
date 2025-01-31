from characters import Characters
import random
HEIGHT = 600

class Comp(Characters):

    def __init__(self, ball, **kwargs):
        super().__init__()
        self.ball = ball
        self.l = False
        self.r = False
        self.difficulty = kwargs.get("difficulty", "medium")

        for key, value in kwargs.items():
            if key == "left" and value == True:
                self.create_char(self.left)
                self.l = True
            elif key == "right" and value == True:
                self.create_char(self.right)
                self.r = True

    def move_char(self):
        if self.l and self.ball.xcor() <= 0:
            self.move_on_difficulty()
        elif self.r and self.ball.xcor() >= 0:
            self.move_on_difficulty()

    def move_on_difficulty(self):
        # ----- Easy AI: random movements
        if self.difficulty == "easy":
            if self.ball.ycor() < self.ycor() and random.choice(range(10)) == 1:
                self.move_down(HEIGHT)
            else:
                self.move_up(HEIGHT)
            if self.ball.ycor() > self.ycor() and random.choice(range(10)) == 1:
                self.move_up(HEIGHT)
            else:
                self.move_down(HEIGHT)
            # Medium AI: Follow the ball with some random
        elif self.difficulty == "medium":
            if self.ball.ycor() < self.ycor() and random.choice([1, 2, 3, 4, 5]) == 1:
                self.move_down(HEIGHT)
            else:
                self.move_up(HEIGHT)
            if self.ball.ycor() > self.ycor() and random.choice([1, 2, 3, 4, 5]) == 1:
                self.move_up(HEIGHT)
            else:
                self.move_down(HEIGHT)
        elif self.difficulty == "impossible":
            # Impossible AI: Follow the ball perfectly
            if self.ball.ycor() < self.ycor():
                self.move_down(HEIGHT)
            elif self.ball.ycor() > self.ycor():
                self.move_up(HEIGHT)
