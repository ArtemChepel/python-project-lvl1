"""Welcome_user func."""
import prompt


def welcome_user():
    """Welcome user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
