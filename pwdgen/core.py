import secrets

class PwdGen:
    """
    A class for generating passwords.

    Raises:
        ValueError: If the given character is not one of !@#* or if the character has a length greater than 1.

    Returns:
        str: The generated password.
    """

    def __init__(self, length=10):
        """
        Initializes the PwdGen object.

        Args:
            length (int, optional): The length of the password to generate. Defaults to 10.
        """
        self.length = length

    def generate_password(self):
        """
        Generates a password.

        Returns:
            str: The generated password.
        """
        charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#*"
        return "".join([secrets.choice(charset) for _ in range(0, self.length)])

    def require_character(self, character):
        """
        Generates a password that contains the given character.

        Args:
            character (str): The character that must be included in the generated password.

        Raises:
            ValueError: If the given character is not one of !@#* or if the character has a length greater than 1.

        Returns:
            str: The generated password that contains the given character.
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
