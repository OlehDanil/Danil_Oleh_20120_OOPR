# tests/test_list_integer_project.py

import pytest
from list_integer_project.list_integer import ListInteger

def test_initialization():
    lst = ListInteger([1, 2, 3])
    assert lst == [1, 2, 3]

    with pytest.raises(TypeError):
        ListInteger([1, 2, 3.5])

def test_setitem():
    lst = ListInteger([1, 2, 3])
    lst[1] = 10
    assert lst[1] == 10

    with pytest.raises(TypeError):
        lst[1] = 10.5

def test_append():
    lst = ListInteger([1, 2, 3])
    lst.append(4)
    assert lst[-1] == 4

    with pytest.raises(TypeError):
        lst.append("5")
