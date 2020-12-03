import random

"""
Welcome to the newest and best text adventure game currently on the market called "The House with a Secret"
"""


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


# Create a monster class
class Monster:
    def __init__(self, room, description, name):
        self.room = room
        self.description = description
        self.name = name


# Create the main function
def main():
    # Create the monster list
    monster_list = []

    # Create and append the monsters(3)
    ogre = Monster(
        2,
        ""
        "\nAll of a sudden you see a dark shadow rush across the wall. "
        "\nAfter a minute of paralyzing fear,"
        "\nYou realize it is a ginormous ogre!!"
        "\nIt's coming at you quick! Either run away or kill it!",
        "Ogre")
    monster_list.append(ogre)

    ghost = Monster(
        13,
        ""
        "\nAll of a sudden the suspicions of a haunting are confirmed as you see a fat, mean ghost come at you."
        "\n Will either the sword or the bow work to kill a ghost?",
        "ghost")
    monster_list.append(ghost)

    witch = Monster(
        3,
        ""
        "\nThe snarling voice continues as you try to escape. You feel something grab your shoulder, "
        "\nbut you break away. You turn to see the face of a disgusting old witch. Do what you can "
        "\nto kill it or escape from it.",
        "witch")
    monster_list.append(witch)

    # Create and append the rooms
    room_list = []

    # Create room 0
    room = Room(
        "You are in the entry way to the abandoned house. "
        "\nYou can investigate the dinning room to the east, the living room to the north, "
        "\nor you may go to the 2nd level",
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
        "\nYou see a suspicious trap door on the floor. You can choose to investigate that, "
        "\nyou may return to the entry hall to the west, or you can choose the doors to the north and east of you.",
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
        "\nQuickly choose to go either north, east, west, northeast, or northwest.",
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
        "\nAs you are looking around when you hear a snarling voice telling you to get out. "
        "\nYou take the advice and choose a door to the north or west.",
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
        "\nowners' ancestors. To the north the complete wall is a window looking out into a huge yard. "
        "\nYou may choose to exit the house onto the deck to the northeast, or continue exploring the house by "
        "\ngoing south or east.",
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
        "\nYou try to use the water, but a thick brown substance comes out instead. "
        "\nTo leave, you can go in any direction except for up, down, northeast, and northwest.",
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
        "\nThis is the stair case downstairs. You are at the bottom of the stairs. You can choose to go back up, or "
        "\nenter the mysterious door by going north.",
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
        "\nhave ever seen in the corner of the room. Oddly, it is the only thing in the house that seems to have "
        "\nbeen perfectly preserved. Take a sit down, or go south, west, or southwest.",
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
        "\nor you can remain outside by going up the staircase to the east.",
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

    # Create room 9
    room = Room(
        "This is a staircase to the 2nd floor deck. Go up west to get to the bottom level or up to get to "
        "\nthe top level.",
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
        "\nentryway, go down.",
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
        "\nThe floor seems like it will give out any second. "
        "\nGet some air to the north, or enter the only room to the southeast.",
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
        "\nor you can go to the lower deck by going down the stairs.",
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
        "\nTo leave, go to the northwest back into the hallway.",
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
        "\nand all you can feel around you is wall and a latter going back up from where you came from. ",
        None,
        None,
        None,
        None,
        1,
        None,
        None,
        None,
        None,
        None, )
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

    # Create the item list
    item_list = []

    # Create and append the items
    item = Item(
        1,
        ""
        "\nYou realize that you are starving. You look at the table and see a roasted turkey. "
        "\nYou find this odd but your hunger is getting worse. Try and pick up the turkey.",
        "turkey")
    item_list.append(item)

    item = Item(
        0,
        ""
        "\nYou see a key lying on the floor. Try and pick it up.",
        "key")
    item_list.append(item)

    item = Item(
        4,
        ""
        "\nYou see a very tattered diary. Your curiosity gets the best of you. Try and pick it up.",
        "diary")
    item_list.append(item)

    item = Item(
        7,
        ""
        "\nA bow and arrow lies in the corner of the room. Grab it in case you need it later.",
        "bow")
    item_list.append(item)

    item = Item(
        3,
        ""
        "\nIn the bedroom, you see a golden plated sword. That may come in use later, pick it up.",
        "sword")
    item_list.append(item)

    item = Item(
        13,

        "\nIn the corner you see a chest. "
        "\nFirst pick it up and then try and open it with a key, if you have one.",
        "chest")
    item_list.append(item)

    # Create the arrow variable
    arrow = 3
    # Create the starting point
    current_room = 0

    # Start of the main program loop
    done = False
    while not done:
        # print the current room description
        print()
        print(room_list[current_room].description)

        # print the items of the current room
        for item in item_list:
            if item.room == current_room:
                print(item.description)

        # print the monster description
        for monster in monster_list:
            if monster.room == current_room:
                print(monster.description)

        # Ask what the user would like to do
        print()
        user_input = input("What is your command? ")
        # Split apart the users input by spaces
        command_words = user_input.split(" ")
        # set up the ability to randomly die
        health = 2
        hurt = random.randrange(10)

        # Allow the user to go north
        if command_words[0].upper() == "NORTH" or command_words[0].upper() == "N":
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room
                # allow the user to die at random times
                if hurt == 10:
                    health -= 1
                    if health == 0:
                        print()
                        print("You are too weak to go on. You will soon die where you are.")
                        done = True

        # Allow the user to go south
        elif command_words[0].upper() == "SOUTH" or command_words[0].upper() == "S":
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room
                # allow the user to die at random times
                if hurt == 10:
                    health -= 1
                    if health == 0:
                        print()
                        print("You are too weak to go on. You will soon die where you are.")
                        done = True

        # Allow the user to go east
        elif command_words[0].upper() == "EAST" or command_words[0].upper() == "E":
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room
                # allow the user to die at random times
                if hurt == 10:
                    health -= 1
                    if health == 0:
                        print()
                        print("You are too weak to go on. You will soon die where you are.")
                        done = True

        # Allow the user to go west
        elif command_words[0].upper() == "WEST" or command_words[0].upper() == "W":
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room
                # allow the user to die at random times
                if hurt == 10:
                    health -= 1
                    if health == 0:
                        print()
                        print("You are too weak to go on. You will soon die where you are.")
                        done = True

        # Allow the user to go up
        elif command_words[0].upper() == "UP" or command_words[0].upper() == "U":
            next_room = room_list[current_room].up
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room
                # allow the user to die at random times
                if hurt == 10:
                    health -= 1
                    if health == 0:
                        print()
                        print("You are too weak to go on. You will soon die where you are.")
                        done = True

        # Allow the user to go down
        elif command_words[0].upper() == "DOWN" or command_words[0].upper() == "D":
            next_room = room_list[current_room].down
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room
                # allow the user to die at random times
                if hurt == 10:
                    health -= 1
                    if health == 0:
                        print()
                        print("You are too weak to go on. You will soon die where you are.")
                        done = True

        # Allow the user to go northeast
        elif command_words[0].upper() == "NORTHEAST" or command_words[0].upper() == "NE":
            next_room = room_list[current_room].northeast
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room
                # allow the user to die at random times
                if hurt == 10:
                    health -= 1
                    if health == 0:
                        print()
                        print("You are too weak to go on. You will soon die where you are.")
                        done = True

        # Allow the user to go northeast
        elif command_words[0].upper() == "NORTHWEST" or command_words[0].upper() == "NW":
            next_room = room_list[current_room].northwest
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room
                # allow the user to die at random times
                if hurt == 10:
                    health -= 1
                    if health == 0:
                        print()
                        print("You are too weak to go on. You will soon die where you are.")
                        done = True

        # Allow the user to go northeast
        elif command_words[0].upper() == "SOUTHEAST" or command_words[0].upper() == "SE":
            next_room = room_list[current_room].southeast
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room
                # allow the user to die at random times
                if hurt == 10:
                    health -= 1
                    if health == 0:
                        print()
                        print("You are too weak to go on. You will soon die where you are.")
                        done = True

        # Allow the user to go northeast
        elif command_words[0].upper() == "SOUTHWEST" or command_words[0].upper() == "SW":
            next_room = room_list[current_room].southwest
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room
                # allow the user to die at random times
                if hurt == 10:
                    health -= 1
                    if health == 0:
                        print()
                        print("You are too weak to go on. You will soon die where you are.")
                        done = True

        # Allow the user to end the game
        elif command_words[0].upper() == "QUIT" or command_words[0].upper() == "Q":
            done = True
            print()
            print("You have left the house. GAME OVER")

        # Allow the user to pick up objects
        elif command_words[0].upper() == "GET":
            get_item = False
            for item in item_list:
                if item.room == current_room and item.name == command_words[1].lower():
                    print()
                    print(f"You have collected the {item.name}.")
                    get_item = True
                    item.room = -1
            if not get_item:
                print()
                print("The item is not in this location.")

        # Allow the user to drop items
        elif command_words[0].upper() == "RELEASE":
            get_item = False
            for item in item_list:
                if item.room == -1 and item.name == command_words[1].lower():
                    print()
                    print("You have released", item.name)
                    get_item = True
                    item.room = current_room
            if not get_item:
                print()
                print("You do not have this item on hand.")

        # Create an inventory
        elif command_words[0].upper() == "INVENTORY" or command_words[0].upper() == "I":
            for item in item_list:
                if item.room == -1:
                    print(item.name)

        # Allow the user to use the sword
        elif command_words[0].upper() == "SWING":
            item_use = False
            for item in item_list:
                if item.room == -1 and command_words[1].lower() == "sword" and item.name == "sword":
                    print()
                    print("You swing the sword.")
                    item_use = True
                    # Allow the user to kill the monsters
                    for monster in monster_list:
                        if monster.room == current_room:
                            print()
                            print("You have killed the creature!")
                            monster.room = -1
            if not item_use:
                print()
                print("You do not have the sword in your possession.")

        # Allow the user to use the bow and arrow
        elif command_words[0].upper() == "USE":
            item_use = False
            for item in item_list:
                if item.room == -1 and command_words[1].lower() == "bow" and item.name == "bow" and arrow > 0:
                    print()
                    print("You load the bow, pull back, and release.")
                    item_use = True
                    arrow -= 1
                    print(f"You have {arrow} arrows remaining")
                    # Allow the user to kill the monsters
                    for monster in monster_list:
                        if monster.room == current_room:
                            print()
                            print("You have killed the creature!")
                            monster.room = -1
                # Create limited arrow use
                elif arrow <= 0:
                    item_use = False
            if not item_use:
                print()
                print("You either do not have the bow in your possession or you have ran out of arrows.")

        # Allow the ability to unlock a chest
        elif command_words[0].upper() == "UNLOCK":
            item_use = False
            for item in item_list:
                if item.room == -1 and command_words[1].lower() == "chest" and item.name == "chest":
                    print()
                    print("You have unlocked the treasure chest. Inside is a boat load of gold coins.")
                    item_use = True
            if not item_use:
                print()
                print("You do not have either the key or the chest in your possession.")

        # Allow the user to open and read a book
        elif command_words[0].upper() == "OPEN":
            item_open = False
            for item in item_list:
                if item.room == -1 and command_words[1].lower() == "book" and item.name == "book":
                    print()
                    print("You open the book and flip to a random page. It reads:"
                          "\"This is day three in this abandoned house. I need to get out of this place. "
                          "\nDo they not know I'm missing yet?\"")
                    item_open = True
                if not item_open:
                    print()
                    print("You do not have the book in your possession.")

        # Allow the user to eat a turkey
        elif command_words[0].upper() == "EAT":
            item_eat = False
            for item in item_list:
                if item.room == -1 and command_words[1].lower() == "turkey" and item.name == "turkey":
                    print()
                    print("You ate a part of the turkey. Your health is back to normal!")
                    item_eat = True
            if not item_eat:
                print()
                print("You do not have the book in your possession.")

        # Create a statement for any inputs that do not match the game
        else:
            print()
            print("The server does not understand what you are trying to do. Please try again.")


# Call the main function 
main()
