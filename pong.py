from turtle import Turtle, Screen
from characters import Characters
from ball import Ball
import random
from scoreboard import Scoreboard
import time
from comp import Comp

WIDTH = 800
HEIGHT = 600

def display_menu(menu, screen):
    menu.clear()
    menu.write("Select Game Mode:\n1. Player 1 vs Computer\n2. Player 1 vs Player 2\n3. Computer vs Computer", align="center", font=("Arial", 16, "normal"))
    screen.update()

def display_difficulty_menu(menu, screen):
    menu.clear()
    menu.write("Select Difficulty Level:\n1. Easy\n2. Medium\n3. Impossible", align="center", font=("Arial", 16, "normal"))
    screen.update()

def start_game(mode, difficulty):
    global game_is_on, sleep
    game_is_on = True
    sleep = 0.1

    character = Characters()
    character.draw_center(HEIGHT)
    ball = Ball()
    score = Scoreboard()

    if mode == "1":  # Player vs Computer
        character_right = Characters()
        character_right.char_right()
        character_left = Comp(ball, left=True, difficulty=difficulty)
    elif mode == "2":  # Player vs Player
        character_right = Characters()
        character_right.char_right()
        character_left = Characters()
        character_left.char_left()
    elif mode == "3":  # Computer vs Computer
        character_right = Comp(ball, right=True, difficulty=difficulty)
        character_left = Comp(ball, left=True, difficulty=difficulty)

    screen.listen()
    if mode == "1": #player vs Computer
        screen.onkeypress(lambda: character_right.move_up(HEIGHT), "Up")
        screen.onkeypress(lambda: character_right.move_down(HEIGHT), "Down")
        screen.onkeypress(lambda: character_right.move_left(WIDTH=WIDTH), "Left")
        screen.onkeypress(lambda: character_right.move_right(WIDTH=WIDTH), "Right")
    elif mode == "2": # Player vs Player
        screen.onkeypress(lambda: character_right.move_up(HEIGHT), "Up")
        screen.onkeypress(lambda: character_right.move_down(HEIGHT), "Down")
        screen.onkeypress(lambda: character_left.move_up(HEIGHT), "w")
        screen.onkeypress(lambda: character_left.move_down(HEIGHT), "s")

    while game_is_on:
        time.sleep(sleep)
        update_screen()
        ball.move()
        update_screen()
        if mode == "1":
            character_left.move_char()
        elif mode == "3":
            character_left.move_char()
            character_right.move_char()

        if ball.distance(character_left) < 50 and ball.xcor() < -360 or ball.distance(character_right) < 50 and ball.xcor() > 360:
            sleep /= 1.2
            ball.bounce_x()

        if ball.xcor() > WIDTH / 2 - 20:
            ball.reset_ball()
            sleep = 0.1
            score.l_point()
            update_screen()

        if ball.xcor() < WIDTH / -2 + 20:
            ball.reset_ball()
            sleep = 0.1
            score.r_point()
            update_screen()

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(WIDTH, HEIGHT)
screen.title("Pong")

def update_screen():
    screen.update()
game_is_on = True
sleep = 0.1





# screen.update()
menu = Turtle()
menu.hideturtle()
menu.penup()
menu.goto(0, 0)
menu.color("white")
# menu.showturtle()

# Display the main menu
display_menu(menu, screen)

# Get user input for game mode
screen.listen()


# noinspection PyGlobalUndefined
def select_mode(mode):
    global selected_mode
    selected_mode = mode
    if mode in ["1", "3"]:  # If computer is involved
        display_difficulty_menu(menu, screen)
        screen.listen()
        screen.onkeypress(lambda: select_difficulty("easy"), "1")
        screen.onkeypress(lambda: select_difficulty("medium"), "2")
        screen.onkeypress(lambda: select_difficulty("impossible"), "3")
    else:
        menu.clear()
        start_game(mode, "medium")  # Default difficulty for player vs player

screen.onkeypress(lambda: select_mode("1"), "1")
screen.onkeypress(lambda: select_mode("2"), "2")
screen.onkeypress(lambda: select_mode("3"), "3")

# Get user input for difficulty if needed
def select_difficulty(difficulty):
    global selected_mode
    menu.clear()
    start_game(selected_mode, difficulty)

screen.listen()
screen.exitonclick()
