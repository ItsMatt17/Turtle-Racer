from turtle import Turtle, Screen
import random

is_race_on = False


s = Screen()
s.setup(width=500, height=400)
s.title("Turtle Racer")


def main():
    """Main Game Function

    Contains main logic for game

    Params:
        None

    Return:
        None

    """

    def play_again(winner: str, has_won: bool) -> None:
        """Handles play again logic (gets user inputs and shows results of game)

        Params:
            winner: str (color of winner turtle)
            has_won: True or False value for if the user picked the correct Turtle

        Return:
            None

        """

        def repeat(again: str):
            """Handles user input to play again

            Params:
                again: str


            """

            if again == "yes" or again == "y":
                s.clear()
                main()  # Restarts game through recursion
            else:
                s.bye()

        if has_won:
            again = s.textinput(
                "Play again",
                f"You won! The color that won was {winner}\nWould you like to play again? 'Yes/No' ",
            ).lower()
            print("You won!")
            repeat(again)

        else:
            again = s.textinput(
                "Play again",
                f"You lost! The color that won was {winner}\nWould you like to play again? 'Yes/No' ",
            ).lower()
        # print("You won!")
        repeat(again)

    START_X, START_Y = (
        -230,
        -100,
    )  # Starting coords for first turtle (Y increased by 35 for each different turtle object)

    user_input = s.textinput(
        title="Make a bet", prompt="Which turtle will win the race? Enter a color:"
    )

    # print(user_input)

    COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtles = []

    for color in COLORS:
        t = Turtle(shape="turtle")
        t.penup()
        t.color(f"{color}")
        t.goto(START_X, START_Y)
        turtles.append(t)
        START_Y += 35

    if user_input:
        is_race_on = True

    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                winner = turtle.pencolor()
                if winner == user_input:
                    play_again(winner, True)

                else:
                    play_again(winner, False)
                is_race_on = False

            distance = random.randint(0, 10)
            turtle.forward(distance)


if __name__ == "__main__":
    main()


s.exitonclick()
