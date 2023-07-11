answer = 9
guess = input('Guess a number between 1 and 10: ')
guess = int(guess)

if guess == answer:
    print('You win!')
else:
    print('Guess again.')
