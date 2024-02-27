import secrets
import string
import math

class PwdGen:
    """
    A class for generating secure and customizable passwords. Ensures the inclusion of at least one lowercase letter,
    one uppercase letter, one digit, and one special character from a specified set, while also allowing for the
    exclusion of any characters the user wishes not to include in the password.
    """
    
    def __init__(self, length=10, exclude_chars=''):
        """
        Initializes the PwdGen object with customizable password length and characters to exclude.
        
        Args:
            length (int): The desired length of the password. Must be at least 4 to ensure inclusion of all required character types.
            exclude_chars (str): A string of characters to exclude from the password.
        """
        self.length = max(length, 4)  # Ensure minimum length of 4 to include all character types
        self.exclude_chars = exclude_chars
        # Define character sets, excluding any user-specified characters
        self.lower = ''.join(c for c in string.ascii_lowercase if c not in exclude_chars)
        self.upper = ''.join(c for c in string.ascii_uppercase if c not in exclude_chars)
        self.digits = ''.join(c for c in string.digits if c not in exclude_chars)
        self.special = ''.join(c for c in "!@#*" if c not in exclude_chars)
        self.charset = self.lower + self.upper + self.digits + self.special

    def generate_password(self):
        """
        Generates a secure password that includes at least one lowercase letter, one uppercase letter, one digit,
        and one special character. The method ensures the password complies with common complexity requirements.
        
        Returns:
            tuple: A tuple containing the generated password and its entropy in bits.
        """
        if len(self.charset) < 4:
            raise ValueError("Character set too small to generate a password with required complexity.")

        # Ensure the password includes at least one character from each category
        pwd_list = [
            secrets.choice(self.lower),
            secrets.choice(self.upper),
            secrets.choice(self.digits),
            secrets.choice(self.special)
        ]

        # Fill the remainder of the password length with random characters from the full charset
        if self.length > 4:
            pwd_list.extend(secrets.choice(self.charset) for _ in range(self.length - 4))

        secrets.SystemRandom().shuffle(pwd_list)  # Shuffle to distribute characters randomly

        pwd = ''.join(pwd_list)
        entropy_bits = self._calculate_entropy(len(pwd))

        return pwd, entropy_bits

    def _calculate_entropy(self, pwd_length):
        """
        Calculates the entropy of the password based on its length and the character set used.
        
        Args:
            pwd_length (int): The length of the password.
            
        Returns:
            float: The entropy of the password in bits.
        """
        N = len(self.charset)  # Number of possible characters
        entropy = pwd_length * math.log2(N)  # Calculate entropy
        return round(entropy, 2)
