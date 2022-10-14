import pytest
from um import count


def test_case():
    assert count("Um, thanks for the album") == 1
    assert count("Hello, Um... um... um... really loved the instrumental") == 3
    assert count("um, thanks for Um... the album") == 2


def test_um_positions():
    assert count("um, Hello, my name is Harman.") == 1
    assert count("my name is Harman Um?") == 1
    assert count("UM... thanks for the album.") == 1
    assert count("UMM... thanks for the album.") == 0


def test_um_edge_cases():
    assert count("Um? Hello, um, thanks for the album.") == 2
    assert count("UM!, um, what's your name?") == 2
