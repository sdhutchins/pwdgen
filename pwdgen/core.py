# -*- coding: utf-8 -*-
import secrets

import logzero


class PwdGen:
    """[summary]

    :raises ValueError: [description]
    :return: [description]
    :rtype: [type]
    """

    def __init__(self, length=10):
        """[summary]

        :param length: [description], defaults to 10
        :type length: int, optional
        """
        self.length = length

    def generate_password(self):
        """[summary]

        :return: [description]
        :rtype: [type]
        """
        charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#*"
        return "".join([secrets.choice(charset) for _ in range(0, self.length)])

    def require_character(self, character):
        """[summary]

        :param character: [description]
        :type character: str
        :raises ValueError: [description]
        :return: [description]
        :rtype: [type]
        """
        pwd = self.generate_password()
        iteration = 1
        if len(character) > 1:
            raise ValueError("Character should be length of 1.")
        elif character not in "!@#*":
            raise ValueError("Character should be one of !@#*")
        while character not in pwd:
            pwd = self.generate_password()
            iteration += 1

        return pwd
