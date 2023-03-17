import random

dash = "-" * 40

prompt = "Pick a number between 1 and 10:   "

value_error = "\nSorry you entered an invalid input. Please try again with an integer between 1 and 10!\n"

play_again_prompt = "Would you like to play again? [y]es/[n]o:  "

scores = []

def start_game():
    number = random.randint(1, 10)
    tries = 1
    guess = 0
    while guess != number:
        guess = input(prompt)
        try:
            guess = int(guess)
        except ValueError:
            print(value_error)
        except TypeError:
            guess = int(guess)
        else:
            if guess >= 1 and guess <= 10:
                if guess > number:
                    print("It is lower!")
                    tries += 1
                if guess < number:
                    print("It is higher!")
                    tries += 1
            else:
                print("\nSorry, please enter a number between 1 and 10!\n")
    scores.append(tries)
    if tries == 1:
        print("\nYou got it! It took you {} try.".format(tries))
    else:
        print("\nYou got it! It took you {} tries.".format(tries))


print(dash, "\nWelcome to the Number Guessing Game!\n{}".format(dash))        
start_game()
high_score = min(scores)
play_again = input(play_again_prompt)
while play_again.lower() == 'y':
    print("\nThe HIGHSCORE is {}.".format(high_score))
    start_game()
    play_again = input(play_again_prompt)
    high_score = min(scores)
print("Game Over. Thanks for playing.")