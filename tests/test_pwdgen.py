import pytest

from pwdgen.core import PwdGen

@pytest.fixture
def pwd_gen():
    return PwdGen()

def test_pwd_gen_initialization(pwd_gen):
    assert isinstance(pwd_gen, PwdGen)
    assert pwd_gen.length == 10

def test_generate_password(pwd_gen):
    password = pwd_gen.generate_password()
    assert isinstance(password, str)
    assert len(password) == pwd_gen.length

def test_require_character(pwd_gen):
    password = pwd_gen.require_character("!")
    assert "!" in password

def test_require_character_invalid_character(pwd_gen):
    with pytest.raises(ValueError) as exc:
        pwd_gen.require_character("invalid")
    assert str(exc.value) == "Character should be one of !@#*"

def test_require_character_character_too_long(pwd_gen):
    with pytest.raises(ValueError) as exc:
        pwd_gen.require_character("invalidcharacter")
    assert str(exc.value) == "Character should be length of 1."
