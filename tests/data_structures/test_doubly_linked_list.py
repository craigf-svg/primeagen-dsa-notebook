from data_structures.history_tree.doubly_linked_list import DoublyLinkedList
import pytest


def test_append():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    assert dll.to_list() == [1, 2, 3]
    assert dll.length == 3


def test_prepend():
    dll = DoublyLinkedList()
    dll.prepend(1)
    dll.prepend(2)
    dll.prepend(3)
    assert dll.to_list() == [3, 2, 1]
    assert dll.length == 3


def test_insert_at():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(3)
    dll.insert_at(2, 1)
    assert dll.to_list() == [1, 2, 3]
    assert dll.length == 3


def test_remove_single_node():
    dll = DoublyLinkedList()
    dll.append(2)
    dll.remove(2)
    assert dll.head == None
    assert dll.tail == None
    assert dll.length == 0


def test_get_returns_correct_node():
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    node = dll.get_idx(1)
    assert node.data == 20


def test_get_idx_raises_on_negative_index():
    dll = DoublyLinkedList()
    dll.append(1)
    with pytest.raises(IndexError):
        dll.get_idx(-1)


def test_get_idx_raises_on_index_out_of_bounds():
    # Only valid indices are 0 and 1
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    with pytest.raises(IndexError):
        dll.get_idx(2)

def test_remove_last():
    dll = DoublyLinkedList()
    dll.append('a')
    dll.append('as')
    dll.append('asd')
    dll.append('asdf')
    assert dll.to_list() == ['a', 'as', 'asd', 'asdf']
    dll.remove_last()
    assert dll.to_list() == ['a', 'as', 'asd']
    dll.remove_last()
    assert dll.to_list() == ['a', 'as']
    dll.remove_last()
    assert dll.to_list() == ['a']
    dll.remove_last()
    assert dll.to_list() == []


def test_to_list():
    dll = DoublyLinkedList()
    assert dll.to_list() == []
    dll.append('a')
    assert dll.to_list() == ['a']
    dll.append('b')
    assert dll.to_list() == ['a', 'b']
    dll.remove_last()
    assert dll.to_list() == ['a']
    dll.remove_last()
    assert dll.to_list() == []


def test_str():
    dll = DoublyLinkedList()
    assert str(dll) == 'None'
    dll.append('b')
    print(str(dll))
    assert str(dll) == 'b -> None'
    dll.remove_last()
    print(str(dll))
    assert str(dll) == 'None'
