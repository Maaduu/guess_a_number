
from random import randint
number_to_guess = randint(1, 25)
number_try = 5

i = 0
i = int(i)
while i < number_try:
    attempt = input('Enter a number ({0} attempt): '.format(i + 1))
    attempt = int(attempt)

    if attempt < number_to_guess:
        print('The number to guess is bigger than {0}'.format(attempt))
    elif attempt > number_to_guess:
        print('The number to guess is smaller than {0}'.format(attempt))
    elif attempt == number_to_guess:
        print('Bravooo! You have won in {0} attempt(s)'.format(
            i + 1))
        break
    i += 1
if attempt != number_to_guess:
    print('You lost.')
    print('The number to guess was: {0}'.format(number_to_guess))
print('Game over.')
