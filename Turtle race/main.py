import turtle
import random
from tkinter import messagebox, simpledialog


def start_race():
    # 1. Setup the Screen
    screen = turtle.Screen()
    screen.setup(width=600, height=400)
    screen.title("The Ultimate Turtle Derby")

    # 2. Get User Input via GUI pop-ups
    num_turtles = simpledialog.askinteger("Input", "How many turtles are racing? (2-10):", minvalue=2, maxvalue=10)

    if not num_turtles:
        return

    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray", "cyan"]
    available_colors = colors[:num_turtles]

    user_bet = simpledialog.askstring("Make your bet",
                                      f"Which color will win? \n({', '.join(available_colors)}):").lower()

    # 3. Initialize Turtles
    all_turtles = []
    y_start = -100
    spacing = 200 / (num_turtles - 1)

    for i in range(num_turtles):
        new_turtle = turtle.Turtle(shape="turtle")
        new_turtle.color(available_colors[i])
        new_turtle.penup()
        # Position turtles at the left edge
        new_turtle.goto(x=-280, y=y_start + (i * spacing))
        all_turtles.append(new_turtle)

    # 4. The Race Logic
    is_race_on = True
    while is_race_on:
        for t in all_turtles:
            # Move each turtle by a random amount
            distance = random.randint(0, 10)
            t.forward(distance)

            # Check for win condition (right edge is at x=300, turtle is 40px wide)
            if t.xcor() > 270:
                is_race_on = False
                winning_color = t.pencolor()

                if winning_color == user_bet:
                    messagebox.showinfo("Race Over", f"You won! The {winning_color} turtle finished first!")
                else:
                    messagebox.showinfo("Race Over", f"You lost! The {winning_color} turtle finished first.")
                break

    screen.exitonclick()


if __name__ == "__main__":
    start_race()
