from app.get_digits import get_digits

def test_get_digits():
    input = "0fg3y5!78hw578!"

    assert get_digits(input) == 3578578

def test_get_digits_with_empty_string_returns_none():
    input = ""

    assert get_digits(input) is None
