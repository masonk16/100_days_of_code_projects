from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    """Creates scoreboard for game."""

    def __init__(self):
        """Initializes position and appearance aspects of scoreboard."""
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates scoreboard"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Called when the game is over."""
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        """Increases score by 1 and clears previous score from game screen."""
        self.score += 1
        self.clear()
        self.update_scoreboard()
