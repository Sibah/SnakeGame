from turtle import Screen, Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_block = Turtle("square")
        new_block.color("white")
        new_block.penup()
        new_block.goto(pos)
        self.segments.append(new_block)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[seg - 1].xcor()
            newY = self.segments[seg - 1].ycor()
            self.segments[seg].goto(newX, newY)

        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)