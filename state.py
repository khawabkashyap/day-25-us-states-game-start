from turtle import Turtle


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def show_on_map(self, name, position):
        self.goto(position)
        self.write(f"{name}")
