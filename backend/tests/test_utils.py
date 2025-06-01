import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))
from utils import add


def test_add_integers():
    assert add(1, 2) == 3


def test_add_strings():
    assert add("a", "b") == "ab"
