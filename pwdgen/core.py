import secrets
import string
import math

class PwdGen:
    """
    A class for generating secure and customizable passwords with an option to exclude specific characters.
    
    Attributes:
        length (int): Desired length of the generated password.
        exclude_chars (str): Characters to be excluded from the password.
        charset (str): Available characters for password generation, derived based on exclusions.
    """
    
    def __init__(self, length=10, exclude_chars=''):
        """
        Initializes the PwdGen object with customizable password length and characters to exclude.
        
        Args:
            length (int, optional): The desired length of the password. Defaults to 10.
            exclude_chars (str, optional): A string of characters to exclude from the password. Defaults to ''.
        """
        self.length = length
        self.exclude_chars = exclude_chars
        self.charset = self._create_charset()

    def _create_charset(self):
        """
        Creates the character set used for password generation, excluding any characters specified by the user.
        
        Returns:
            str: The character set used for password generation.
        """
        base_charset = string.ascii_letters + string.digits + "!@#*"
        return ''.join([char for char in base_charset if char not in self.exclude_chars])

    def generate_password(self, include_chars=''):
        """
        Generates a secure password, ensuring it includes specified characters and avoiding predictable patterns.
        Additionally calculates and returns the entropy of the generated password.
        
        Args:
            include_chars (str, optional): Characters that must be included in the generated password. Defaults to ''.
        
        Returns:
            tuple: A tuple containing the generated password and its entropy in bits.
        """
        if any(char not in self.charset for char in include_chars):
            raise ValueError("All include_chars must be in the allowed charset.")

        pwd_list = [secrets.choice(self.charset) for _ in range(self.length)]
        pwd_list = self._avoid_predictable_patterns(pwd_list)

        for i, char in enumerate(include_chars):
            pwd_list[i] = char

        secrets.SystemRandom().shuffle(pwd_list)

        pwd = ''.join(pwd_list)
        entropy_bits = self._calculate_entropy(len(pwd))

        return pwd, entropy_bits

    def _calculate_entropy(self, pwd_length):
        """
        Calculates the entropy of a password given its length and the character set used.
        
        Args:
            pwd_length (int): The length of the password.
        
        Returns:
            float: The entropy of the password in bits.
        """
        N = len(self.charset)
        entropy = pwd_length * math.log2(N)
        return round(entropy, 2)

    def _avoid_predictable_patterns(self, pwd_list):
        """
        Modifies the password list to avoid predictable patterns such as sequential characters.
        
        Args:
            pwd_list (list): The list of characters that make up the password.
        
        Returns:
            list: The modified list of characters with predictable patterns avoided.
        """
        for i in range(1, len(pwd_list)):
            while pwd_list[i] == pwd_list[i-1]:
                pwd_list[i] = secrets.choice(self.charset)
        return pwd_list

    def require_character(self, character):
        """
        Generates a password that contains the given character. This method utilizes the generate_password method
        to ensure the inclusion of specific characters and calculate entropy.
        
        Args:
            character (str): The character that must be included in the generated password.
        
        Returns:
            tuple: A tuple containing the generated password that includes the given character and its entropy in bits.
        """
        return self.generate_password(include_chars=character)
