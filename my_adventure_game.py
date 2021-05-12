import time
import random


def print_pause(message):
    print(message)
    time.sleep(1)


def print_item(text, item):
    print(text, item)
    time.sleep(1)


def intro():
    print_pause("\nYou find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a dragon is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.\n")


def field(items, random_item):
    print_pause("Do you want to knock on the door of the house"
                " or peer into the cave?")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")

    response = input("What would you like to do? Please enter 1 or 2: \n")

    if response == '1':
        "\n"
        house(items, random_item)
    elif response == '2':
        cave(items, random_item)
    else:
        print("Please enter a valid response")
        field(items, random_item)


def house(items, random_item):
    if random_item not in items:
        print_pause("\nYou approach the door of the house.")
        print_pause("You are about to knock when the door opens"
                    " and out steps a dragon.")
        print_pause("Yikes! This is the dragon's house!")
        print_pause("The dragon attacks you!")
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny dagger.\n")
        fight_or_flight(items, random_item)
    else:
        print_pause("\nYou approach the door of the house.")
        print_pause("You are about to knock when the door opens"
                    " and out steps a dragon.")
        print_pause("This is the dragon's house...")
        print_item("But you come prepared with", random_item)
        print_pause("The dragon attacks you!")
        fight_or_flight(items, random_item)


def fight_or_flight(items, random_item):

    response = input("\nWould you like to (1) fight or (2) run away?\n")

    if response == '1':
        fight(items, random_item)
    elif response == '2':
        if random_item in items:
            print_pause("\nWhy are you running away, you scaredy-cat?")
            print_item("You now have the most powerful weapon,", random_item)
            fight_or_flight(items, random_item)
        else:
            print("\nYou run back into the field."
                  "Luckily, you don't seem to have been followed.\n")
            field(items, random_item)
    else:
        print("Please enter a valid response")
        fight_or_flight(items, random_item)


def cave(items, random_item):
    if random_item not in items:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_item("You have found", random_item)
        print_item("You discard your silly old dagger"
                   " and take the", random_item)
        print_pause("You walk back out to the field.\n")
        items.append(random_item)
        field(items, random_item)
    else:
        print_item("\nYou already have", random_item)
        print_pause("There's nothing else to find in the cave.")
        print_pause("You're now ready to enter the house.\n")
        field(items, random_item)


def fight(items, random_item):
    if random_item not in items:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the pirate.")
        play_again(items, random_item)
    else:
        print_item("\nAs the dragon moves to attack, you unveil", random_item)
        print_item(random_item, "shines brightly in your hand"
                   " as you brace yourself for the attack.")
        print_pause("But the dragon takes one look at your"
                    " shiny new toy and runs away!")
        print_pause("You have rid the town of the dragon. You are victorious!")
        play_again(items, random_item)


def play_again(items, random_item):
    print_pause("\nGAME OVER!")
    response = input("\nWould you like to play again? (y/n)\n")
    if 'y' in response:
        items.clear()
        print_pause("Excellent choice, this is a great game!")
        play_game()
    else:
        print_pause("\nThanks for playing! See you next time.")


def play_game():
    items = []
    magical_items = ["The Sword of Ogoroth", "The Mace of Wizardor",
                     "The Axe of Asgarth"]
    random_item = random.choice(magical_items)
    intro()
    field(items, random_item)


play_game()
