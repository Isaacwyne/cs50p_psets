import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar1 = Jar(24)
    assert jar1.capacity == 24
    with pytest.raises(ValueError):
        jar2 = Jar(-12)
        jar2.capacity


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(6)
    assert jar.size == 11
    with pytest.raises(ValueError):
        jar.deposit(12)


def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(5)
    assert jar.size == 6
    jar.withdraw(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(10)
