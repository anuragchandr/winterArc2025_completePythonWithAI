from testing import get_weather,add,divide
import pytest
#unittest for get_weather function
# def test_get_weather():
#     assert get_weather(35) == "It's a hot day" # wrong if we change hot to cold
#     assert get_weather(5) == "It's a cold day"
#     assert get_weather(20) == "It's a moderate day"
#Testing in python using Pytest framework

#@pytest.fixture #specially used for OOPs 
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, -3) == 2
    assert divide(5, 2) == 2.5

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)