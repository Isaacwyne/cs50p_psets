import pytest
from seasons import validate_date


def test_validate_date():
    validate_date("1994-10-10") == ("1994", "10", "10")
    with pytest.raises(ValueError):
        validate_date("October 10, 1994")
    with pytest.raises(ValueError):
        validate_date("1994/10/10")
    with pytest.raises(ValueError):
        validate_date("1994-7-07")
