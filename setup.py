""" This is the setup.py script for setting up the package and fulfilling any
necessary requirements.

References:
https://github.com/pypa/sampleproject/blob/master/setup.py
https://github.com/biopython/biopython/blob/master/setup.py
http://python-packaging.readthedocs.io/en/latest/index.html
"""
# Modules Used
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path
import os

# Set the home path of the setup script/package
__version__ = '0.0.2'
project_path = os.path.dirname(os.path.abspath(__file__))
project_name = os.path.basename(project_path)
project_url = 'https://github.com/sdhutchins/pwdgen'


def readme():
    """Get the long description from the README file."""
    with open(path.join(project_path, 'README.md'), encoding='utf-8') as f:
        return f.read()


# Setup the package by adding information to these parameters
setup(
    name=project_name,
    author='Shaurita D. Hutchins',
    author_email='sdhutchins@outlook.com',
    description="A command-line password generator.",
    version=__version__,
    long_description=readme(),
    url=project_url,
    license='MIT',
    keywords='password generator cli',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Framework :: Cookiecutter'
    ],
    # Packages will be automatically found if not in this list.
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    install_requires=[
   'logzero',
    ],
    entry_points={
        'console_scripts': ['pwdgen=pwdgen.cli:main'],
    },
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose']
)
