# Create the room class
class Room:
    def __init__(self, description, north, south, east, west, up, down, northeast, northwest, southeast, southwest):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.northeast = northeast
        self.northwest = northwest
        self.southeast = southeast
        self.southwest = southwest


# Create an item class
class Item:
    def __init__(self, room, description, name):
        self.room = room
        self.description = description
        self.name = name


def main():
    item_list = []

    item = Item(
        7,
        "You see a comfortable looking chair in the corner. If you want, take a rest.",
        "chair")
    item_list.append(item)

    item = Item(
        1,
        "You see a key lying on the floor. Try and pick it up.",
        "key")
    item_list.append(item)

    item = Item(
        5,
        "You are thirst for some water. Try turning on the sink.",
        "sink")
    item_list.append(item)

    item = Item(
        3,
        "In the bedroom, you see a golden plated sword. That may come in use later, pick it up.",
        "sword")
    item_list.append(item)

    item = Item(
        13,
        "In the corner you see a chest. If you have a key, try and open it up.",
        "chest")
    item_list.append(item)

    room_list = []

    # Create room 0
    room = Room(
        "You are in the entry way to the abandoned house. "
        "You can investigate the dinning room to the east, the living room to the north, "
        "or you may go to the 2nd level",
        4,
        None,
        1,
        None,
        10,
        None,
        5,
        None,
        None,
        None)
    room_list.append(room)

    # Create room 1
    room = Room(
        "You have reached the dinning room. The floorboards squeak with every step. "
        "You see a suspicious trap door on the floor. You can choose to investigate that, "
        "you may return to the entry hall to the west, or you can choose the doors to the north and east of you.",
        5,
        None,
        2,
        0,
        None,
        14,
        None,
        4,
        None,
        None)
    room_list.append(room)

    # Create room 2
    room = Room(
        "You have entered a dimly lit hallway. The walls appear to be closing in on you and you want to get out fast. "
        "Quickly choose to go either north, east, west, northeast, or northwest.",
        6,
        None,
        3,
        1,
        None,
        None,
        7,
        5,
        None,
        None)
    room_list.append(room)

    # Create room 3
    room = Room(
        "You stumble into what appears to be a bedroom. "
        "As you are looking around you hear a snarling voice telling you to get out. "
        "You take the advice and choose a door to the north or west.",
        7,
        None,
        None,
        2,
        None,
        None,
        None,
        None,
        None,
        None)
    room_list.append(room)

    # Create room 4
    room = Room(
        "You enter the living room of the abandoned house. The walls are filled with creepy paintings of the house's "
        "owners' ancestors. To the north the complete wall is a window looking out into a huge yard. "
        "You may choose to exit the house onto the deck to the northeast, or continue exploring the house by "
        "going south or east.",
        None,
        0,
        5,
        None,
        None,
        None,
        8,
        None,
        1,
        None)
    room_list.append(room)

    # Create room 5
    room = Room(
        "You have entered the bathroom of the abandoned house. "
        "You try to use the water, but a thick brown substance comes out instead. "
        "To leave, you can go in any direction except for up, down, northeast, and northwest.",
        8,
        1,
        6,
        4,
        None,
        None,
        None,
        None,
        2,
        0)
    room_list.append(room)

    # Create room 6
    room = Room(
        "After opening the door you stumble down a set of stairs. "
        "This is the stair case downstairs. You are at the bottom of the stairs. You can choose to go back up, or "
        "enter the mysterious door by going north.",
        15,
        None,
        None,
        None,
        2,
        None,
        None,
        None,
        None,
        None)
    room_list.append(room)

    # Create room 7
    room = Room(
        "You enter what appears to have once been a man cave. You see the most comfortable looking lazy boy you "
        "have ever seen in the corner of the room. Oddly, it is the only thing in the house that seems to have "
        "been perfectly preserved. Take a sit down, or go south, west, or southwest.",
        None,
        3,
        None,
        6,
        None,
        None,
        None,
        None,
        None,
        2)
    room_list.append(room)

    # Create room 8
    room = Room(
        "You go outside on the deck to get some fresh air. You can go back into the house by going south or southwest, "
        "or you can remain outside by going up the staircase to the east.",
        None,
        5,
        9,
        None,
        None,
        None,
        None,
        None,
        None,
        4)
    room_list.append(room)

    # Room 9
    room = Room(
        "This is a staircase to the 2nd floor deck. Go up west to get to the bottom level or up to get to "
        "the top level.",
        None,
        None,
        None,
        12,
        None,
        8,
        None,
        None,
        None,
        None)
    room_list.append(room)

    # Create a upstairs room 10
    room = Room(
        "You are at the top of the stairs on the 2nd floor. To go into the hallway, go north. To go back to the "
        "entryway, go down.",
        11,
        None,
        None,
        None,
        None,
        0,
        None,
        None,
        None,
        None)
    room_list.append(room)

    # Create room 11
    room = Room(
        "You have entered the 2nd floor hallway. The hallway smells of mold and rotting wood. "
        "The floor seems like it will give out any second. "
        "Get some air to the north, or enter the only room to the southeast.",
        12,
        10,
        None,
        None,
        None,
        None,
        None,
        None,
        13,
        None)
    room_list.append(room)

    # Create Room 12
    room = Room(
        "You have entered the upper deck on the 2nd floor. You can either go into the house by going south, "
        "or you can go to the lower deck by going down the stairs.",
        None,
        11,
        9,
        None,
        None,
        None,
        None,
        None,
        None,
        None)
    room_list.append(room)

    # Create Room 13
    room = Room(
        "You have entered the upstairs bedroom. They say this room is haunted. "
        "To leave, go to the northwest back into the hallway.",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        11,
        None,
        None)
    room_list.append(room)

    # Create a downstairs room 14
    room = Room(
        "You went down the trap door and are in a pitch black, very enclosed area. You feel your surroundings, "
        "and all you can feel around you is wall and a latter going back up from where you came from. ",
        None,
        None,
        None,
        None,
        1,
        None,
        None,
        None,
        None,
        None,)
    room_list.append(room)

    # Create the basement AKA room 15
    room = Room(
        "You enter the basement and search for a light. Go up to get back to the hallway on the main level.",
        None,
        None,
        None,
        None,
        2,
        None,
        None,
        None,
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
        for item in item_list:
            if item.room == current_room:
                print(item.description)

        user_input = input("What direction would you like to go? ")
        room_choice = user_input

        # Allow the user to go north
        if room_choice.upper() == "NORTH" or room_choice.upper() == "N":
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go south
        elif room_choice.upper() == "SOUTH" or room_choice.upper() == "S":
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go east
        elif room_choice.upper() == "EAST" or room_choice.upper() == "E":
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go west
        elif room_choice.upper() == "WEST" or room_choice.upper() == "W":
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go up
        elif room_choice.upper() == "UP" or room_choice.upper() == "U":
            next_room = room_list[current_room].up
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go down
        elif room_choice.upper() == "Down" or room_choice.upper() == "D":
            next_room = room_list[current_room].down
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go northeast
        elif room_choice.upper() == "Northeast" or room_choice.upper() == "NE":
            next_room = room_list[current_room].northeast
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go northeast
        elif room_choice.upper() == "Northwest" or room_choice.upper() == "NW":
            next_room = room_list[current_room].northwest
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go northeast
        elif room_choice.upper() == "Southeast" or room_choice.upper() == "SE":
            next_room = room_list[current_room].southeast
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go northeast
        elif room_choice.upper() == "Southwest" or room_choice.upper() == "SW":
            next_room = room_list[current_room].southwest
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
