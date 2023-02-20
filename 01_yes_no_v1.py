

# Ask the user if they have played before
show_intructions = input("Have you played this game before? ").lower()

# If they say yes, output 'program continues'

yes_answers = ["yes", "y"]
no_answers = ["no", "n"]

if show_intructions in yes_answers:
    print("program continues")

elif show_intructions in no_answers:
    print("Display instructions")

# If they say no, output 'display instructions'
else:
    print("Please answer yes / no")


