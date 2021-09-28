import math
import pytest
from pylinkedlist import CircularLinkedList
from pylinkedlist.math import sqrt, remainder, root


# test fixtures for fun
def test_print(capture_stdout):
    print("hello, world")
    assert capture_stdout["stdout"] == "hello, world\n"


# skip a test
@pytest.mark.skip(reason="this is inachieveable")
def test_one_is_two():
    assert 1 == 2


# mark test passed
@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1


# test multiple inputs (easier)
@pytest.mark.parametrize(
    "test_input, expected",
    [
        (1 + 1, 2),
        (1 + 2, 3),
        (1 - 2, -1),
    ],
)
def test_multi_slaps(test_input, expected):
    assert test_input == expected


""" Actual tests starts here """
num = 22341341242234134124
num2 = 138
num3 = 14.387623
num4 = 0.01

num_2 = 2
num2_2 = 32
num3_2 = -23.5678
num4_2 = 0


def test_sqrt(get_random_number):
    assert round(sqrt(num), 8) == round(math.sqrt(num), 8)
    assert round(sqrt(num2), 8) == round(math.sqrt(num2), 8)
    assert round(sqrt(num3), 8) == round(math.sqrt(num3), 8)
    assert round(sqrt(get_random_number), 8) == round(math.sqrt(get_random_number), 8)


def test_remainder():
    assert remainder(num, num_2) == num % num_2
    assert remainder(num2, num2_2) == num2 % num2_2
    assert remainder(num3, num3_2) == num3 % num3_2

    # test error raising using context manager
    with pytest.raises(ZeroDivisionError):
        remainder(num4, num4_2)


def test_root():
    assert root(num, num_2) == num ** (1 / float(num_2))
    assert root(num2, num2_2) == num2 ** (1 / float(num2_2))
    assert root(num3, num3_2) == num3 ** (1 / float(num3_2))
    with pytest.raises(ZeroDivisionError):
        root(num4, num4_2)


def test_circular_linked_list():
    test_data = [3, 23.234, -21.3, "e", False, tuple]
    circular_linked_list = CircularLinkedList()
    circular_linked_list.add(test_data)
    assert circular_linked_list.head.data == test_data[0]
    assert circular_linked_list.head.next.data == test_data[1]
    assert circular_linked_list.tail.next.data == test_data[0]
    assert list(circular_linked_list) == test_data
    assert str(circular_linked_list) == test_data.__str__()

    another_cll = CircularLinkedList()
    assert another_cll.head.data is None
    assert list(another_cll) == []

    another_cll.add("1")
    another_cll.add(2)
    assert another_cll.head.data == "1"


"""
if __name__ == "__main__":
    pytest.main()

"""
