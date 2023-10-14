from my_lib.functions import fahrenheit_to_celsius


# pytest parametrize
def test_return_value_with_f32():
    returned = fahrenheit_to_celsius(f=32)
    expected = 0

    assert returned == expected
