# Monty Hall problem
import random

# Array with prizes of the doors


def random_door():
    doors = ["goat", "goat", "goat"]
    doors[random.randint(0, 2)] = "prize"
    return doors

# Monty Hall open a door


def open_door(player_sel, doors):
    open = player_sel
    if (doors[player_sel] == "prize"):
        open = random.randint(0, 2)
        while (open == player_sel):
            open = random.randint(0, 2)
        doors[open] = "open"
    else:
        index = doors.index("prize")
        while ((open == player_sel) or (open == index)):
            open = random.randint(0, 2)
        doors[open] = "open"

    return doors


def main():

    attemps = 1000000
    victories = 0
    defeats = 0

    for i in range(attemps):
        # Generate the doors
        doors = random_door()

        # Player selects the door
        player_selection = random.randint(0, 2)

        # Monty Hall opens a door with a goat
        doors = open_door(player_selection, doors)

        # Player changes of door
        if (player_selection == doors.index("prize")):
            player_selection = doors.index("goat")

        elif (player_selection == doors.index("goat")):
            player_selection = doors.index("prize")

        # Count of victories and defeats
        if doors[player_selection] == "prize":
            victories = victories + 1
        else:
            defeats = defeats + 1

    print(f"{attemps} attemps")
    print(f"You won {victories} times.")
    print(f"You lost {defeats} times.")

    print("Win percentage: {:.2f}%".format(((victories/attemps)*100)))


if __name__ == "__main__":
    main()
