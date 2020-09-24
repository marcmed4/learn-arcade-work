# Lab 4: Shark Game
import random


def main():
    # Define the variables used in the game.
    miles_traveled = 0
    dolphin_tiredness = 0
    hunger = 0
    fish = 3
    shark_miles = -20

    # Introduction to the game.
    print("Welcome to Shark!")
    print("You have stolen a shark's treasure and are attempting to swim your way across the Atlantic Ocean.")
    print("The shark you stole the treasure from wants it back and is chasing you down!")
    print("Survive your vast ocean trek and out swim the shark to safety!")
    print()

    # Boolean variable used to create the game.
    done = False
    while not done:

        print("A. Eat fish for fuel.")
        print("B. Swim ahead at moderate speed.")
        print("C. Swim ahead at full speed.")
        print("D. Stop on a raft for the night.")
        print("E. Status Check.")
        print("Q. Quit.")
        print()

        # Ask the user what their input will be.
        user_input = input("What will you do? ")

        # Allow the option for the user to quit.
        if user_input.upper() == "Q" and not done:
            done = True
            print("You have ended the game.")
            print("The shark regained his treasure and you are lost at sea.")
            print()

        # Allow the user to select a status input.
        elif user_input.upper() == "E" and not done:
            print("Miles Traveled:", miles_traveled)
            print("Fish Remaining:", fish)
            print("The shark is", miles_traveled - shark_miles, "miles behind you.")
            print()

        # Allow the user to stop for the night.
        elif user_input.upper() == "D" and not done:
            print("You stop on a raft for the night.")
            print("The dolphin is happy!")
            print("The shark keeps going!")
            print()
            dolphin_tiredness = 0
            shark_miles += random.randrange(7, 14, 1)

        # Allow the user to swim at full speed ahead.
        elif user_input.upper() == "C" and not done:
            miles = random.randrange(10, 20, 1)
            miles_traveled += miles
            hunger += 1
            dolphin_tiredness += random.randrange(1, 3, 1)
            shark_miles += random.randrange(7, 14, 1)
            island = random.randrange(20)
            if island == 10 and not done:
                hunger = 0
                dolphin_tiredness = 0
                fish = 3
                print("As you traveled you came across an island!")
                print("You stop and go fishing, fill up on food, and")
                print("your dolphin has time to rest and play!")
                print("The shark continued to chase you down.")
                print()
            else:
                print("You swam ahead full speed moving a total of", miles, "miles!")
                print("Your hunger increases.")
                print("The shark continues the hunt!")
                print()

        # Allow the user to swim at moderate speed ahead.
        elif user_input.upper() == "B" and not done:
            miles = random.randrange(5, 12, 1)
            miles_traveled += miles
            hunger += 1
            dolphin_tiredness += 1
            shark_miles += random.randrange(7, 14, 1)
            island = random.randrange(20)
            if island == 10 and not done:
                hunger = 0
                dolphin_tiredness = 0
                fish = 3
                print("As you traveled you came across an island!")
                print("You stop and go fishing, fill up on food, and")
                print("your dolphin has time to rest and play!")
                print("The shark continued to chase you down.")
                print()
            else:
                print("You swam ahead at moderate speed moving a total of", miles, "miles!")
                print("Your hunger increases.")
                print("The shark continues the hunt!")
                print()

        # Allow the user to eat fish for fuel.
        elif user_input.upper() == "A" and not done:
            if fish > 0 and not done:
                fish -= 1
                hunger = 0
                print("You eat some fish!")
                print()
            else:
                print("You have ran out of fish and hunger pains are setting in.")
                print()

        # Status updates for the game.
        # Status update for hunger.
        if hunger > 6 and not done:
            print("You died of hunger!")
            print("Game Over!")
            print()
            done = True
        elif hunger > 4 and not done:
            print("You are very hungry!")
            print("Get some fish!")
            print()

        # Status update for distance traveled/win check.
        if miles_traveled >= 200:
            print("Congratulations! You have swam across the entire Atlantic Ocean!")
            print("You win! You get to keep the treasure!")
            print()
            done = True

        # Status update for dolphin's tiredness.
        if dolphin_tiredness > 8 and not done:
            print("Your dolphin died of exhaustion!")
            print("With no dolphin, the shark will catch up to you and eat you")
            print("on the spot.")
            print("Game Over.")
            print()
            done = True
        elif dolphin_tiredness > 5 and not done:
            print("Your dolphin is very tired!")
            print()

        # Status update for shark's distance.
        if miles_traveled - shark_miles <= 0:
            print("The shark has caught up to you!")
            print("It eats you and your dolphin and takes its treasure back")
            print("Game Over!")
            print()
            done = True
        elif miles_traveled - shark_miles < 15 and not done:
            print("You see a large mass swimming towards you.")
            print("The shark is getting close!")
            print("Keep swimming ahead!")
            print()


main()
