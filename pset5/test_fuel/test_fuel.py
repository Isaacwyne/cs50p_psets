import pytest
from fuel import convert, gauge


def test_convert():
    assert convert('1/2') == 50
    assert convert('3/4') == 75
    assert convert('1/4') == 25
    assert convert('9/9') == 100
    with pytest.raises(ValueError):
        convert('100/2')
    with pytest.raises(ZeroDivisionError):
        convert('2/0')


def test_gauge():
    assert gauge(100) == 'F'
    assert gauge(75) == '75%'
    assert gauge(25) == '25%'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
