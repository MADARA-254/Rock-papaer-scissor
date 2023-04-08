import random

players = 0
computers = 0
choices = ['rock', 'paper', 'scissor']

while True:
    player = input("Enter either Rock Paper Or scissor or q to quit :").lower()

    if player == "q":
        break

    if player not in choices:
        continue

    computer = random.choice(choices)
    print(f'computer picked: {computer}')

    if player == 'rock' and computer == 'scissor':
        print('You won')
        players += 1


    elif player == 'paper'and computer == 'rock':
        print('You won')
        players += 1
        

    elif player == 'scissor'and computer == 'paper':
        print('You won')
        players += 1

    
    elif player == computer:
        print('You draw')

    else:
        print('computer won')
        computers += 1

    print(f"you won: {players} Computer won: {computers}")
print('Goodbye')