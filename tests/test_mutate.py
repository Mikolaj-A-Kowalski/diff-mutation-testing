# test_mutate.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from mutate import mutate_line, mutate_candidates


def test_plus_to_minus():
    result = mutate_line("test.py", 1, "x = 1 + 2")
    assert result == ("test.py", 1, "x = 1 + 2", "x = 1 - 2")


def test_minus_to_plus():
    result = mutate_line("test.py", 2, "y = 5 - 3")
    assert result == ("test.py", 2, "y = 5 - 3", "y = 5 + 3")


def test_no_mutation():
    result = mutate_line("test.py", 3, "z = 42")
    assert result is None


def test_mutate_candidates():
    candidates = [
        ("f.py", 1, "a = b + c"),
        ("f.py", 2, "d = e - f"),
        ("f.py", 3, "print('hello')"),
    ]
    result = mutate_candidates(candidates)
    assert len(result) == 2
    assert ("f.py", 1, "a = b + c", "a = b - c") in result
    assert ("f.py", 2, "d = e - f", "d = e + f") in result
