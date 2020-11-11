print("Hello world.")
print("Ben is wearing a blue shirt. I like it.")
print("Ben is my roommate. \tHe is also in CMSC.")
print("I like to run.")
print("I asked Ben if he wanted to go running. He responded: \"no way.\"")
print("\tIt is weird he does not like to run.")
print("Cross-country\nis\nthe\nbest\nsport!")
print("""The other day
we did a repeat 1000 meter workout.
It was tough,
but a good run.""")


import random


def selection_sort(my_list):
    """ Sort a list using the selection sort """

    # Loop through the entire array
    outside_loop_selection = 0
    inside_loop_selection = 0
    for cur_pos in range(len(my_list)):
        outside_loop_selection += 1
        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos

        # Scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(my_list)):
            inside_loop_selection += 1

            # Is this position smallest?
            if my_list[scan_pos] < my_list[min_pos]:
                # It is, mark this position as the smallest
                min_pos = scan_pos

        # Swap the two values
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp
        inside_loop_selection += 1
    print("The outside loop ran", str(outside_loop_selection), "times.")
    print("The inside loop ran", str(inside_loop_selection), "times.")


def insertion_sort(my_list):
    """ Sort a list using the insertion sort """

    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    outside_loop_insertion = 0
    inside_loop_insertion = 0
    for key_pos in range(1, len(my_list)):
        outside_loop_insertion += 1

        # Get the value of the element to insert
        key_value = my_list[key_pos]

        # Scan from right to the left (start of list)
        scan_pos = key_pos - 1

        # Loop each element, moving them up until
        # we reach the position the
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            inside_loop_insertion += 1
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1

        # Everything's been moved out of the way, insert
        # the key into the correct location
        my_list[scan_pos + 1] = key_value

    print("The outside loop ran", str(outside_loop_insertion), "times.")
    print("The inside loop ran", str(inside_loop_insertion), "times.")


# This will point out a list
# For more information on the print formatting {:3}
# see the chapter on print formatting.
def print_list(my_list):
    for item in my_list:
        print(f"{item:3}", end="")
    print()


def main():
    # Create two lists of the same random numbers
    list_for_selection_sort = []
    list_for_insertion_sort = []
    list_size = 100
    for i in range(list_size):
        new_number = random.randrange(100)
        list_for_selection_sort.append(new_number)
        list_for_insertion_sort.append(new_number)

    # Print the original list
    print("Original List")
    print_list(list_for_selection_sort)

    # Use the selection sort and print the result
    print("Selection Sort")
    selection_sort(list_for_selection_sort)
    print_list(list_for_selection_sort)

    # Use the insertion sort and print the result
    print("Insertion Sort")
    insertion_sort(list_for_insertion_sort)
    print_list(list_for_insertion_sort)


main()