
show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = input("Have you played this game before? ").lower()

    # If they say yes, output 'program continues'

    yes_answers = ["yes", "y"]
    no_answers = ["no", "n"]

    if show_instructions in yes_answers:
        print("program continues")

    elif show_instructions in no_answers:
        print("Display instructions")

    # If they say no, output 'display instructions'
    else:
        print("Please answer yes / no")


