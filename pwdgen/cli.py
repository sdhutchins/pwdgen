# -*- coding: utf-8 -*-
import argparse

from pwdgen.core import PwdGen


def pwdgen_func(length, character=None):
    pwdgen = PwdGen(length=length)
    if character:
        pwd = pwdgen.require_character(character=character)
    else:
        pwd = pwdgen.generate_password()
    return pwd


def main():
    parser = argparse.ArgumentParser(description='Test')
    parser.add_argument(
        '-l', '--length', help='Define a length for your password.', default=10, type=int)
    parser.add_argument(
        '-c', '--character', help='Select a required character.', default=None)
    args = parser.parse_args()

    pwd = pwdgen_func(length=args.length, character=args.character)

    print(pwd)


if __name__ == '__main__':
    main()
