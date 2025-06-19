from data_structures.MyQueue import MyQueue


def test_initial_queue():
    q = MyQueue()
    assert q.data == []


def test_is_empty():
    q = MyQueue()
    assert q.empty() == True
    q.enqueue(5)
    assert q.empty() == False


def test_shift_adds_elements():
    q = MyQueue()
    q.enqueue('D')
    q.enqueue('A')
    assert q.data == ['D', 'A']


def test_pop_removes_and_returns_first():
    q = MyQueue()
    q.enqueue('A')
    val = q.dequeue()
    assert val == 'A'
    assert q.data == []
