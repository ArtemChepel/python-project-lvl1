"""Welcome_user func."""
import prompt


def welcome_user():
    """Welcome.

    Returns:
           username: string.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def main():
    """Call welcome function."""
    welcome_user()


if __name__ == '__main__':
    main()
