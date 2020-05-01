import random
secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

for guess_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    
    if guess > secret_number:
        print('Your guess is too high!')
    elif guess < secret_number:
        print('Your guess is too low!')
    else:
        break

if guess == secret_number:
    print('good job! You guessed my number in %d guesses!'%secret_number)
else:
    print('Nope, The number is ' + str(secret_number))
