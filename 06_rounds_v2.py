import random
# set balance for testing purposes
balance = 5

rounds_played = 0

print()
play_again = input("Please press <enter> to play ")
while play_again == "":
    # increase the number of rounds played
    rounds_played += 1

    # print the round number
    print()
    print(f'*** Round #{rounds_played}***')
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
