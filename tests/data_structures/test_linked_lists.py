from data_structures.linked_list import Node, LinkedList


def test_create():
    node_a = Node('A')
    node_b = Node('B')
    node_a.next = node_b
    node_c = Node('C')
    node_b.next = node_c
    ll = LinkedList()
    ll.head = node_a
    assert ll.head.data == 'A'


def test_insert_at_end():
    ll = LinkedList()
    ll.insert_at_end('First')
    ll.insert_at_end('Second')
    assert str(ll) == 'First -> Second -> None'


def test_delete_at_end():
    ll = LinkedList()
    ll.insert_at_end('First')
    ll.insert_at_end('Second')
    ll.insert_at_end('Third')
    ll.delete_last()
    assert str(ll) == 'First -> Second -> None'



def test_insert_at_start():
    node_a = Node('A')
    ll = LinkedList()
    ll.head = node_a
    ll.insert_at_start('Z')
    assert str(ll) == 'Z -> A -> None'


def test_delete_match():
    node_a = Node('A')
    node_b = Node('B')
    node_a.next = node_b
    ll = LinkedList()
    ll.head = node_a
    ll.delete_matched_first('A')
    assert ll.head.data == 'B'
