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

# Room 9
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
