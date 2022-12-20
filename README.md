[![Build Status](https://travis-ci.com/sdhutchins/pwdgen.svg?branch=master)](https://travis-ci.com/sdhutchins/pwdgen)
[![This package is currently under development.](https://img.shields.io/badge/under-development-orange.svg)](https://github.com/sdhutchins/pwdgen)

# pwdgen

A command-line password generator that allows you to select the length of your password as well as any required character you may want in the password.

This password generator fits most if not all standard password requirements in that it requires both uppercase and lowercase alphabets, numbers, and at least one non-alphanumeric character.

## Background

It's pretty simple. I was looking for a way to easily generate passwords for myself.

## Installation

View the below methods for installing this package.

### GitHub

1.  Download the zip file and unzip it or `git clone
    https://github.com/sdhutchins/pwdgen.git`
2.  `cd pwdgen`
3.  `pip install .`

**OR**

`pip install git+https://github.com/sdhutchins/pwdgen.git`

## Examples

### Generate a Password of 20 characters

```console
user@host:~$ pwdgen -l 20
vuvmnWQFf5Wazcl#nRri
```
### Generate a Password of 20 characters with an Exclamation

```console
user@host:~$ pwdgen -l 20 -c !
EIxfcjGKeuwlqy!lF5zI
```

### Help Output

```console
user@host:~$ pwdgen --help
usage: pwdgen [-h] [-l LENGTH] [-c CHARACTER]

Test

optional arguments:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        Define a length for your password.
  -c CHARACTER, --character CHARACTER
                        Select a required character.
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
