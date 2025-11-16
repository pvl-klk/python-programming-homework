from Tests.src.heap_sort import heap_sort


def test_sort_empty_list() -> None:
    assert heap_sort([]) == []


def test_sort_single_element() -> None:
    assert heap_sort([5]) == [5]
    assert heap_sort([-1]) == [-1]
    assert heap_sort([0]) == [0]


def test_sort_positive_numbers() -> None:
    assert heap_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_sort_negative_numbers() -> None:
    assert heap_sort([-3, -1, -4, -1, -5]) == [-5, -4, -3, -1, -1]
    assert heap_sort([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]


def test_sort_mixed_numbers() -> None:
    assert heap_sort([3, -1, 0, -2, 5]) == [-2, -1, 0, 3, 5]
    assert heap_sort([0, -1, 1, -2, 2]) == [-2, -1, 0, 1, 2]


def test_sort_strings() -> None:
    assert heap_sort(["banana", "apple", "cherry"]) == ["apple", "banana", "cherry"]
    assert heap_sort(["z", "a", "m"]) == ["a", "m", "z"]
