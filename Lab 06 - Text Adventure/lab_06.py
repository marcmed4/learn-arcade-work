class Room:
    def __init__(self, description, north, south, east, west):
        self.description = ""
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0


def main():
    room_list = []

    room = Room(
        "You have entered the Kitchen. Mom is making Tacos. Wash you hands in the bathroom to the East",
        4,
        None,
        1,
        None)
    room_list.append(room)

    room = Room(
        "You have reached the bathroom. Make sure to wash your hands to prevent the spread of Covid-19.",
        5,
        None,
        2,
        0),
    room_list.append(room)

    room = Room(
        "You are in your bedroom. Give yourself a rest before heading to you indoor basketball hoop to the East.",
        6,
        None,
        3,
        1)
    room_list.append(room)

    room = Room(
        "You entered the indoor gym. Shoot some hoops before dinner, but don't bother your sister to the North.",
        7,
        None,
        None,
        2)
    room_list.append(room)

    room = Room(
        "You are now in your sister's room and you two are fighting. Mom tells you to knock it off.",
        None,
        3,
        None,
        6)
    room_list.append(room)

    room = Room(
        "You just entered the game room. You play some Call of Duty to pass the time until dinner.",
        8,
        2,
        7,
        5)
    room_list.append(room)

    room = Room(
        "You sneak into your parent's bedroom. If you get caught you'll be grounded for a month! Be careful!",
        8,
        1,
        6,
        4)
    room_list.append(room)

    room = Room(
        "You arrive in the dining room. Help your parents by setting the table for dinner.",
        None,
        0,
        5,
        None)
    room_list.append(room)

    room = Room(
        "You go outside on the porch. Lay in the hammock and relax. You deserve it!",
        None,
        5,
        None,
        None)
    room_list.append(room)

    room = Room(
        "You go outside on the porch. Lay in the hammock and relax. You deserve it!",
        None,
        6,
        None,
        None)
    room_list.append(room)

    current_room = 0

    print(room_list[current_room].description)


main()
