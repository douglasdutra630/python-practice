def guessing_game():
    while True: 
        print('What is your Guess?')
        guess = input()

        if guess == '97':
            print('You got it. F*#ing finally!')
            return False
        else:
            print(f' No, {guess} is not it. Try again idiot!\n')

guessing_game()
