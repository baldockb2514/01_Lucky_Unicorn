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
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
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


# Main routine goes here...
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    print()
    instructions()

# Ask user how much they want to play with...

print()
how_much = num_check("How much do you want to play with? ", 0, 10)
print("You will be spending ${}".format(how_much))
