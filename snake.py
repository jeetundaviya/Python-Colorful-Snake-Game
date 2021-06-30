import random
import time
import turtle as t


class Snake:
    game_is_on = True
    starting_seg = [(0, 0), (-20, 0), (-40, 0)]
    food_location = (0, 0)
    score = 0
    new_score = t.Turtle(visible=False)
    game_over_mssg = t.Turtle(visible=False)

    level = t.textinput("Level","Difficulty level ?(E/H)")[0].upper()
    speed = t.textinput("Speed","Snake's Speed ? (S/M/H)")[0].upper()

    segments = []

    screen = t.Screen()

    def pause_play(self):
        self.game_over_mssg.clear()
        if not self.game_is_on:
            self.game_is_on = True
            self.start_game()
        elif self.game_is_on:
            self.game_is_on = False
        print(self.game_is_on)

    def create_snake_and_food(self):

        for _ in range(0, 3):
            new_seg = t.Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(self.starting_seg[_])
            self.segments.append(new_seg)

    def move_forward(self):
        for block_index in range(len(self.segments) - 1, 0, -1):
            previous_x = self.segments[block_index - 1].xcor()
            previous_y = self.segments[block_index - 1].ycor()
            self.segments[block_index].penup()
            self.segments[block_index].goto(previous_x, previous_y)

        self.segments[0].forward(20)

    def move_left(self):
        self.segments[0].left(90)

    def move_right(self):
        self.segments[0].right(90)

    def start_game(self):

        self.getFoodBall()

        snake_speed = 0.1
        if self.speed == "H":
            snake_speed = 0.01
        elif self.speed == "M":
            snake_speed = 0.1
        else:
            snake_speed = 0.5

        if self.level == "H":

            while self.game_is_on and not self.gameover():
                # while self.game_is_on:

                self.screen.update()
                time.sleep(snake_speed)
                if self.isFoodBallEaten():
                    self.getFoodBall()
                    # self.getFoodBall()

                for _ in self.segments[1:]:
                    if abs(_.pos()[0] - self.segments[0].pos()[0]) <= 10 and abs(
                            _.pos()[1] - self.segments[0].pos()[1]) <= 10:
                        print("Snake ate itself Game Over !")
                        self.game_over_mssg.penup()
                        self.game_over_mssg.color("White")
                        self.game_over_mssg.goto(0, 0)
                        self.game_over_mssg.write("GAME OVER", move=False, align="center", font=("Verdana",
                                                                                                 30, "normal"))
                        self.game_is_on = False
                        break
                self.move_forward()
            self.game_over_mssg.penup()
            self.game_over_mssg.color("White")
            self.game_over_mssg.goto(0, 0)
            self.game_over_mssg.write("GAME OVER", move=False, align="center", font=("Verdana",
                                                                                     30, "normal"))
        else:
            while self.game_is_on and not self.disable_gameover_with_touch_walls():
                # while self.game_is_on:

                self.screen.update()
                time.sleep(snake_speed)
                if self.isFoodBallEaten():
                    self.getFoodBall()
                    # self.getFoodBall()

                for _ in self.segments[1:]:
                    if abs(_.pos()[0] - self.segments[0].pos()[0]) <= 10 and abs(
                            _.pos()[1] - self.segments[0].pos()[1]) <= 10:
                        print("Snake ate itself Game Over !")
                        self.game_over_mssg.penup()
                        self.game_over_mssg.color("White")
                        self.game_over_mssg.goto(0,0)
                        self.game_over_mssg.write("GAME OVER", move=False, align="center", font=("Verdana",
                                                                                                             30, "normal"))
                        self.game_is_on = False
                        break
                self.move_forward()


    def disable_gameover_with_touch_walls(self):
        if self.segments[0].ycor() >= 320:
            print('Game Over')
            self.segments[0].goto(self.segments[0].xcor(), -320)
            print('stopping for positive y')
            # return True
            return False
        elif self.segments[0].ycor() <= -320:
            print('Game Over')
            self.segments[0].goto(self.segments[0].xcor(), 320)
            print('stopping for negitive y')
            # return True
            return False
        elif self.segments[0].xcor() >= 370:
            print('Game Over')
            self.segments[0].goto(-370, self.segments[0].ycor())
            print('stopping for positive x')
            # return True
            return False
        elif self.segments[0].xcor() <= -370:
            print('Game Over')
            self.segments[0].goto(370, self.segments[0].ycor())
            print('stopping for negitive x')
            # return True
            return False
        else:
            return False

    def gameover(self):
        if self.segments[0].ycor() >= 320:
            print('Game Over')
            self.segments[0].goto(self.segments[0].xcor(), -320)
            return True

        elif self.segments[0].ycor() <= -320:
            print('Game Over')
            self.segments[0].goto(self.segments[0].xcor(), 320)
            print('stopping for negitive y')
            return True
        elif self.segments[0].xcor() >= 370:
            print('Game Over')
            self.segments[0].goto(-370, self.segments[0].ycor())
            print('stopping for positive x')
            return True
        elif self.segments[0].xcor() <= -370:
            print('Game Over')
            self.segments[0].goto(370, self.segments[0].ycor())
            print('stopping for negitive x')
            return True
        else:
            return False

    def getScore(self):
        pass

    def screen_settings(self):

        self.screen.title("Snake Game")
        self.screen.screensize(700, 600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.listen()

    def getFoodBall(self):
        t.shape("circle")
        t.penup()
        self.food_location = (random.randint(-350, 350), random.randint(-300, 300))
        t.goto(self.food_location)
        t.colormode(255)
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        t.color(random_color)
        print(self.food_location)

    def isFoodBallEaten(self):
        food_x = self.food_location[0]
        food_y = self.food_location[1]
        snake_mouth_x = self.segments[0].xcor()
        snake_mouth_y = self.segments[0].ycor()
        print("diffis :- x : " + str(round(abs(food_x - self.segments[0].xcor()))) + ",y : " + str(
            round(abs(food_y - self.segments[0].ycor()))))
        # for
        if (round(abs(food_x - self.segments[0].xcor())) < 15) & (round(abs(food_y - self.segments[0].ycor())) < 15):
            print(self.segments[0].pos())
            print('food eaten')
            print('eaten on for positive y')
            t.goto(self.food_location)
            t.dot(20, "black")
            new_turtle = t.Turtle("square")
            t.colormode(255)
            self.score += 1

            self.new_score.clear()
            self.new_score.penup()
            self.new_score.goto(0, 300)
            self.new_score.color("white")
            self.new_score.write("Score : " + str(self.score), move=False, align="center", font=("Verdana",
                                                                                            15, "normal"))
            new_turtle.color(int(t.color()[1][0]), int(t.color()[1][1]), int(t.color()[1][2]))
            self.segments.append(new_turtle)

            return True

        else:
            return False

    def screen_key_listeners(self):
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeypress(self.move_right, "Right")
        self.screen.onkeypress(self.move_left, "Up")
        self.screen.onkeypress(self.move_right, "Down")
        self.screen.onkeypress(self.pause_play, "space")

    def __init__(self):

        self.screen_settings()
        self.screen_key_listeners()
        self.create_snake_and_food()
        self.start_game()

        self.screen.exitonclick()
