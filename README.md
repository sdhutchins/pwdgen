[![Build Status](https://app.travis-ci.com/sdhutchins/pwdgen.svg?branch=master)](https://app.travis-ci.com/sdhutchins/pwdgen)
[![This package is currently under development.](https://img.shields.io/badge/under-development-orange.svg)](https://github.com/sdhutchins/pwdgen)

# pwdgen

A command-line password generator that allows users to customize password length and exclude specific characters. This tool ensures generated passwords include at least one lowercase letter, one uppercase letter, one digit, and one special character, adhering to common password policies.

## Background

The motivation behind `pwdgen` was simple: to develop a convenient method for generating secure, complex passwords. In a digital age where security is paramount, having a tool that can quickly create passwords meeting various security standards is invaluable.

## Features

**Customizable Length**: Users can define the exact length of their password, enabling the creation of passwords that meet the security requirements of different systems.

**Excludable Characters**: `pwdgen` allows users to specify characters they wish to exclude from the password, further customizing the password to meet specific user or system requirements.

**Comprehensive Character Set**: By default, `pwdgen` generates passwords that include a balanced mix of uppercase and lowercase letters, numbers, and special characters. This ensures the generation of strong passwords that comply with most password policies.

**Security Focused**: Leveraging a cryptographically secure pseudorandom number generator, `pwdgen` guarantees the uniqueness and security of each password, minimizing the risk of password-related security breaches.

**Verbose Output**: For users interested in the security details of their generated passwords, `pwdgen` offers a verbose option that includes the password entropy in the output, providing insight into the password's strength.

## Installation

View the below methods for installing this package.

### GitHub

1. Download the zip file and unzip it or `git clone
    https://github.com/sdhutchins/pwdgen.git`
2. `cd pwdgen`
3. `pip install .`

**OR**

`pip install git+https://github.com/sdhutchins/pwdgen.git`

## Examples

### Generate a Password of 20 characters with an Exclamation

```console
user@host:~$ pwdgen -l 20 -c !
EIxfcjGKeuwlqy!lF5zI
```

### Help Output

```console
user@host:~$ pwdgen --help
usage: pwdgen [-h] [-l LENGTH] [-c CHARACTER] [-e EXCLUDE] [-v]

pwdgen is a command-line password generator.

options:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        Define a length for your password
  -c CHARACTER, --character CHARACTER
                        Select a required character from: !@#*
  -e EXCLUDE, --exclude EXCLUDE
                        Characters to exclude from the password
  -v, --verbose         Display verbose output, including password entropy
```

## Tests

To run tests, type `pytest` in the
pwdgen directory after installing pytest on your system or in your environment.

## Author

Shaurita D. Hutchins · [@sdhutchins](https://github.com/sdhutchins)
    · [sdhutchins@outlook.com](mailto:sdhutchins@outlook.com)

## Contributing

If you would like to contribute to this package, install the package in
development mode, and check out our [contributing
guidelines](https://github.com/sdhutchins/pwdgen/blob/master/CONTRIBUTING.rst).

## License

[MIT](https://github.com/sdhutchins/pwdgen/blob/master/LICENSE)
