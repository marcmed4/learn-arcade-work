# Create the room class
class Room:
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


def main():
    room_list = []

    # Create room 0
    room = Room(
        "You have entered the Kitchen. Mom is making Tacos."
        " Wash you hands in the bathroom to the east or set the table to the north.",
        4,
        None,
        1,
        None)
    room_list.append(room)

    # Create room 1
    room = Room(
        "You have reached the bathroom. Make sure to wash your hands to prevent the spread of Covid-19. "
        "There are doors to the north, east, and west of you.",
        5,
        None,
        2,
        0)
    room_list.append(room)

    # Create room 2
    room = Room(
        "You are in your bedroom. Give yourself a rest before heading to you indoor basketball hoop to the east "
        "or the game room to your north.",
        6,
        None,
        3,
        1)
    room_list.append(room)

    # Create room 3
    room = Room(
        "You entered the indoor gym. Shoot some hoops before dinner, but don't bother your sister to the north. "
        "You could also return to your room to the west.",
        7,
        None,
        None,
        2)
    room_list.append(room)

    # Create room 4
    room = Room(
        "You arrive in the dining room. Help your parents by setting the table for dinner. Or get a pre-meal snack "
        "from the kitchen to the south. Remember, your parents do not like you in their room to the east.",
        None,
        0,
        5,
        None)
    room_list.append(room)

    # Create room 5
    room = Room(
        "You sneak into your parent's bedroom. If you get caught you'll be grounded for a month! Be careful! "
        "Escape in any direction!",
        8,
        1,
        6,
        4)
    room_list.append(room)

    # Create room 6
    room = Room(
        "You just entered the game room. You play some Call of Duty to pass the time until dinner. "
        "You can also head out to the porch to the north to enjoy the weather.",
        8,
        2,
        7,
        5)
    room_list.append(room)

    # Create room 7
    room = Room(
        "You are now in your sister's room and you two are fighting. Mom tells you to knock it off or you will not "
        "be able to go to the indoor gym to the south or the game room to the west anymore.",
        None,
        3,
        None,
        6)
    room_list.append(room)

    # Create room 8
    room = Room(
        "You go outside on the porch. Lay in the hammock and relax. You deserve it! You can remain outside by going "
        "east, or risk going into your parent's room to the south.",
        None,
        5,
        None,
        None)
    room_list.append(room)

    # Extend room 8
    room = Room(
        "You go outside on the porch. Lay in the hammock and relax. You deserve it! You can remain outside by going "
        "west, or go south to your game room.",
        None,
        6,
        None,
        None)
    room_list.append(room)

    # Create the starting point
    current_room = 0

    # Create the boolean variable
    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        user_input = input("What direction would you like to go? ")
        room_choice = user_input

        # Allow the user to go North
        if room_choice.upper() == "NORTH" or room_choice.upper() == "N":
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go South
        elif room_choice.upper() == "SOUTH" or room_choice.upper() == "S":
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go East
        elif room_choice.upper() == "EAST" or room_choice.upper() == "E":
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go West
        elif room_choice.upper() == "WEST" or room_choice.upper() == "W":
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to end the game
        elif room_choice.upper() == "QUIT" or room_choice.upper() == "Q":
            done = True
            print()
            print("You have left the house. GAME OVER")

        # Create a statement for any inputs that do not match the game
        else:
            print()
            print("The server does not understand what you are trying to do. Please try again.")


main()
