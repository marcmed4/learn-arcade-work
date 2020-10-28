import re


def main():

    # This function takes in a line of text and returns
    # a list of words in the line.
    def split_line():
        return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

    spelling_reference = open("dictionary.txt")

    spelling_reference_list = []
    for line in spelling_reference:
        line = line.strip()
        spelling_reference_list.append(line)

    spelling_reference.close()

    # Linear Search
    print("---Linear Search---")
    chapter = open("AliceInWonderLand200.txt")

    current_line_position = 0
    for line in chapter:
        current_line_position += 1
        word_list = split_line()
        for word in word_list:
            i = 0
            key = word.upper()
            while i < len(spelling_reference_list) and spelling_reference_list[i] != key:
                i += 1

            if i == len(spelling_reference_list):
                print("On line", str(current_line_position), "there is a possible misspelled word:", word)

    chapter.close()

    print("---Binary Search---")
    chapter = open("AliceInWonderLand200.txt")

    current_line_position = 0
    for line in chapter:
        current_line_position += 1
        word_list = split_line()
        for word in word_list:
            lower_bound = 0
            upper_bound = len(spelling_reference_list) - 1
            found = False
            key = word.upper()
            while lower_bound <= upper_bound and not found:
                middle_pos = (lower_bound + upper_bound) // 2

                if spelling_reference_list[middle_pos] < key:
                    lower_bound = middle_pos + 1
                elif spelling_reference_list[middle_pos] > key:
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print("On line", str(current_line_position), "there is a possible misspelled word:", word)

    chapter.close()


main()
