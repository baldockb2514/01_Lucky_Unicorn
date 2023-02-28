# set balance for testing purposes
balance = 5

rounds_played = 0

print()
play_again = input("Please press <enter> to play ")
while play_again == "":
    # increase the number of rounds played
    rounds_played += 1

    # print the round number
    print(f'*** Round #{rounds_played}***')
    balance -= 1
    print(f"Balance = ${balance:.2f}")
    print()

    if balance < 1:
        play_again = "xxx"
        print("You have run out of money")
    else:
        play_again = input("Press <enter> to play again or type anything to quit. ")
        print()


print(f'Final balance = ${balance:.2f}')
