import random


# Functions go here...

# checks user response is yes/no to a given question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

            # If they say no, output 'display instructions'

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


# Displays instructions
def instructions():
    statement_decorator("How to Play", "*")
    print()
    print("Choose a starting amount (minimum $1, maximum $10).")
    print()
    print("Then press <enter> to play. You will get either a horse, a zebra, a donkey or a unicorn.")
    print()
    print("It costs $1 per round. Depending on your prize you might get some of the money back Here's the payout "
          "amounts...")
    print("Unicorn: $5,00 (balance increases by $4.00)")
    print("Horse: $0.50 (balance decreases by $0.50)")
    print("Zebra: $0.50 (balance decreases by $0.50)")
    print("Donkey: $0.00 (balance decreases by $1.00")
    print()
    print("can you avoid the donkeys, get the unicorns and walk home with the money??")
    print()
    print("Hint: to quit while you're ahead, type any key instead of pressing <enter>")
    return ""


# Checks users enter a integer between a low and high number
def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))

            # is the response is too low / high, give
            if low < response <= high:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


# Add decoration to a statement
def statement_decorator(statement, decoration):
    # Make string with three characters
    sides = decoration * 3

    # add decoration to start and ent of statement
    statement = "{} {} {}".format(sides, statement, sides)
    # Make the decoration above and below the statement the same length as the statement
    top_bottom = decoration * len(statement)

    # add decoration to the to and bottom of the statement
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routine goes here...
print()
statement_decorator("Welcome to the Lucky Unicorn Game", "*")
print()
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    print()
    instructions()

# Ask user how much they want to play with...
print()
statement_decorator("Let's get Started...", "-")
how_much = num_check("How much do you want to play with? $", 0, 10)

balance = how_much

rounds_played = 0

play_again = input("Please press <enter> to play ")
while play_again == "":
    # increase the number of rounds played
    rounds_played += 1

    # print the round number
    print()
    statement_decorator(f"Round #{rounds_played}", ".")
    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5, user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    # if the random # is between 6 and 36, user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    # if the number is either a horse or zebra, subtract $0.50 from the balance
    else:
        # if the number is even, set the chosen token to horse
        if chosen_num % 2 == 0:
            chosen = "horse"
        # otherwise set the token to zebra
        else:
            chosen = "zebra"
        balance -= 0.5
    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))

    if balance < 1:
        play_again = "xxx"
        print("You have run out of money")
    else:
        play_again = input("Press <enter> to play again or type anything to quit. ")
        print()

print(f'Final balance = ${balance:.2f}')
