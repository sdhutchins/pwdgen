import argparse
import logzero
from pwdgen.core import PwdGen

def generator(length, exclude_chars='', verbose=False):
    """
    Generates a password using the PwdGen class, with options to exclude certain characters and optionally display entropy.
    
    Args:
        length (int): The length of the password to generate.
        exclude_chars (str, optional): Characters to exclude from the password.
        verbose (bool, optional): Whether to display verbose output, including password entropy.
    
    Returns:
        str: The generated password, and optionally prints entropy if verbose is True.
    """
    pwdgen = PwdGen(length=length, exclude_chars=exclude_chars)
    try:
        pwd, entropy = pwdgen.generate_password()
        if verbose:
            logzero.logger.info(f"Generated Password: {pwd}\nEntropy: {entropy} bits")
        else:
            logzero.logger.info(pwd)
    except ValueError as e:
        logzero.logger.error(e)

def main():
    parser = argparse.ArgumentParser(description='pwdgen is a command-line password generator that ensures each password includes at least one lowercase letter, one uppercase letter, one digit, and one special character.')
    parser.add_argument('-l', '--length', help='Define the length for your password (minimum 4)', default=10, type=int)
    parser.add_argument('-e', '--exclude', help='Characters to exclude from the password', default='')
    parser.add_argument('-v', '--verbose', help='Display verbose output, including password entropy', action='store_true')

    args = parser.parse_args()

    # Invoke the generator function with parsed arguments
    generator(length=args.length, exclude_chars=args.exclude, verbose=args.verbose)

if __name__ == '__main__':
    main()
