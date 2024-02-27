import pytest

from pwdgen.core import PwdGen

def test_length():
    pwd_gen = PwdGen(12)
    pwd, _ = pwd_gen.generate_password()
    assert len(pwd) == 12

def test_exclude_chars():
    exclude = 'abc123'
    pwd_gen = PwdGen(exclude_chars=exclude)
    pwd, _ = pwd_gen.generate_password()
    assert all(c not in exclude for c in pwd)

def test_include_special_chars():
    pwd_gen = PwdGen()
    pwd, _ = pwd_gen.generate_password()
    # Check that at least one of the special characters is included
    assert any(c in pwd for c in "!@#*")

def test_entropy():
    pwd_gen = PwdGen()
    _, entropy = pwd_gen.generate_password()
    assert isinstance(entropy, float)
    # Additional entropy value checks could be added based on expected results
