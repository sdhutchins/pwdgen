import argparse
import logzero
from pwdgen.core import PwdGen

def generator(length, required_character=None):
    """
    Generates a password using the PwdGen class.

    Args:
        length (int): The length of the password to generate.
        required_character (str, optional): The character that must be included in the generated password.

    Returns:
        str: The generated password.
    """
    pwdgen = PwdGen(length=length)
    try:
        if required_character:
            pwd = pwdgen.require_character(character=required_character)
        else:
            pwd = pwdgen.generate_password()
    except ValueError as e:
        logzero.logger.error(e)
        return
    return pwd

def main():
    """
    Command-line entry point for the password generator.
    """
    parser = argparse.ArgumentParser(
        description='pwdgen is a command-line password generator.')
    parser.add_argument(
        '-l', '--length', help='Define a length for your password', default=10, type=int)
    parser.add_argument(
        '-c', '--character', help='Select a required character from: !@#*', default=None)
    args = parser.parse_args()

    pwd = generator(length=args.length, required_character=args.character)

    print(pwd)

if __name__ == '__main__':
    main()
