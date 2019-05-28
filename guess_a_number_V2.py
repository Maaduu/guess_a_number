
from random import randint
amplitude = input('Enter the range of the number to guess: ')
amplitude = int(amplitude)
number_try_input = input('Enter the number of trials: ')
number_try_input = int(number_try_input)
number_to_guess = randint(1, amplitude)
number_try = range(number_try_input)
for i in number_try:
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
if attempt != number_to_guess:
    print('You lost.')
    print('The number to guess was: {0}'.format(number_to_guess))
print('Game over.')
