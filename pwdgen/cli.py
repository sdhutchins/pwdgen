import argparse
import logzero
from pwdgen.core import PwdGen

def generator(length, required_character=None, exclude_chars='', verbose=False):
    """
    Generates a password using the PwdGen class, with options to require or exclude certain characters and optionally display entropy.
    
    Args:
        length (int): The length of the password to generate.
        required_character (str, optional): The character that must be included in the generated password.
        exclude_chars (str, optional): Characters to exclude from the password.
        verbose (bool, optional): Whether to display verbose output, including password entropy.
    
    Returns:
        str: The generated password, and optionally prints entropy if verbose is True.
    """
    pwdgen = PwdGen(length=length, exclude_chars=exclude_chars)
    try:
        pwd, entropy = pwdgen.generate_password(include_chars=required_character)
        if verbose:
            print(f"Generated Password: {pwd}\nEntropy: {entropy} bits")
        else:
            print(pwd)
    except ValueError as e:
        logzero.logger.error(e)

def main():
    """
    Command-line entry point for the password generator.
    """
    parser = argparse.ArgumentParser(description='pwdgen is a command-line password generator.')
    parser.add_argument('-l', '--length', help='Define a length for your password', default=10, type=int)
    parser.add_argument('-c', '--character', help='Select a required character from: !@#*', default=None)
    parser.add_argument('-e', '--exclude', help='Characters to exclude from the password', default='')
    parser.add_argument('-v', '--verbose', help='Display verbose output, including password entropy', action='store_true')

    args = parser.parse_args()

    generator(length=args.length, required_character=args.character, exclude_chars=args.exclude, verbose=args.verbose)

if __name__ == '__main__':
    main()
