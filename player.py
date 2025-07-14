# move the turtle with keypress

#     Create a turtle player that starts at the bottom of the screen and
#     listen for the "Up" keypress to move the turtle north. If you get
#     stuck, check the video walkthrough in Step 3.

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)


    def go_up(self):
        self.forward(MOVE_DISTANCE)


    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


        # this explanation is start line 30
    # Detect when the turtle player has reached the top edge of the screen
    # (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle
    # to the starting position and increase the speed of the cars. Hint: think
    # about creating an attribute and using the MOVE_INCREMENT to increase the
    # car speed. If you get stuck, check the video walkthrough in Step 6.











