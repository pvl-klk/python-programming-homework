import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.heapsort import heapsort

def test_sort_empty_list():
    assert heapsort([]) == []

def test_sort_single_element():
    assert heapsort([5]) == [5]
    assert heapsort([-1]) == [-1]
    assert heapsort([0]) == [0]

def test_sort_positive_numbers():
    assert heapsort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    assert heapsort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_sort_negative_numbers():
    assert heapsort([-3, -1, -4, -1, -5]) == [-5, -4, -3, -1, -1]
    assert heapsort([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]

def test_sort_mixed_numbers():
    assert heapsort([3, -1, 0, -2, 5]) == [-2, -1, 0, 3, 5]
    assert heapsort([0, -1, 1, -2, 2]) == [-2, -1, 0, 1, 2]

def test_sort_strings():
    assert heapsort(['banana', 'apple', 'cherry']) == ['apple', 'banana', 'cherry']
    assert heapsort(['z', 'a', 'm']) == ['a', 'm', 'z']
