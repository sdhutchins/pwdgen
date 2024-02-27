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
        self.length = max(length, 4)  # Ensure minimum length to include at least one special character
        self.exclude_chars = exclude_chars
        self.charset = self._create_charset()

    def _create_charset(self):
        """
        Creates the character set used for password generation, excluding any characters specified by the user.
        
        Returns:
            str: The character set used for password generation.
        """
        base_charset = string.ascii_letters + string.digits + "!@#*"
        return ''.join(char for char in base_charset if char not in self.exclude_chars)

    def generate_password(self):
        """
        Generates a secure password, ensuring it includes at least one required special character.
        
        Additionally calculates and returns the entropy of the generated password.
        
        Args:
            include_chars (str, optional): Characters that must be included in the generated password. Defaults to ''.
        
        Returns:
            tuple: A tuple containing the generated password and its entropy in bits.        
        """
        required_chars = "!@#*"
        # Randomly select one required character
        required_char = secrets.choice(required_chars)
        remaining_length = self.length - 1  # Adjust for the one required character

        # Generate the rest of the password
        pwd_list = [secrets.choice(self.charset) for _ in range(remaining_length)]
        pwd_list.append(required_char)  # Ensure a required special character is included

        secrets.SystemRandom().shuffle(pwd_list)  # Shuffle to distribute the required character randomly
        
        pwd_list = self._avoid_predictable_patterns(pwd_list)

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
