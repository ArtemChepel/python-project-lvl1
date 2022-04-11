"""Even check module."""

from random import randint

import prompt
from brain_games.greeting import welcome_user

name = welcome_user()


def is_even(num):
    """Even check func.

    Args:
        num: integer

    Returns:
        answer: string
    """
    return 'yes' if num % 2 == 0 else 'no'


def quiz():
    """Ask question.

    Returns:
        answer: string
    """
    random_number = randint(1, 100)
    print('Question: {0}'.format(str(random_number)))
    answer = prompt.string('Your answer: ')
    if answer == is_even(random_number):
        print('Correct!')
        return 'Correct!'
    else:
        string = "'{0}' is wrong answer ;(. Correct answer was '{1}'"
        print(string.format(answer, is_even(random_number)))


def game():
    """Iterate quastions."""
    print('Answer "yes" if the number is even, otherwise answer "no".')
    step = 0
    while step <= 3:
        if step == 3:
            print('Congratulations, {0}!'.format(name))
        elif quiz() != 'Correct!':
            print("Let's try again, {0}!".format(name))
            break
        step += 1
