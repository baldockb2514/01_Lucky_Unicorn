import random

# main routine goes here

tokens = ["unicorn", "horse", "horse", "horse", "zebra", "zebra", "zebra", "donkey", "donkey", "donkey"]
BALANCE_START = 100

balance = BALANCE_START

# Testing loop to generate 20 tokens
print()
for item in range(0, 500):
    chosen = random.choice(tokens)

    # Adjust balance
    if chosen == "unicorn":
        balance += 4
    if chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5



# Output
print(f'Starting Balance: ${BALANCE_START:.2f}')
print(f'Final Balance: ${balance:.2f}')
