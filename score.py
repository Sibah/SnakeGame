from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.currentScore = 0
        self.color("white")
        self.penup()

        self.goto(0, 250)
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f"Score: {self.currentScore}", move=False, align="center", font=("Arial", 24, "bold"))

    def increaseScore(self):
        self.currentScore += 1
        self.updateScore()

    def gameOver(self):
        self.clear()
        self.write(f"Score: {self.currentScore}", move=False, align="center", font=("Arial", 24, "bold"))
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=("Arial", 24, "bold"))
