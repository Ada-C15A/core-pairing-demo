from app.get_digits import get_digits

def test_get_digits():
    input = "0fg3y5!78hw578!"

    assert get_digits(input) == 3578578
