from algorithms.bubble_sort import bubble_sort


def test_bubble_sort_unsorted():
    assert bubble_sort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8]


def test_bubble_sort_empty():
    assert bubble_sort([]) == []


def test_bubble_sort_single_element():
    assert bubble_sort([5]) == [5]


def test_bubble_sort_reversed():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]


def test_bubble_sort_duplicate_numbers():
    assert bubble_sort([5, 5, 9, 9, 2, 1]) == [1, 2, 5, 5, 9, 9]
