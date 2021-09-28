from linkedlistpy import (
    LinkedList,
    DoublyLinkedList,
    CircularLinkedList,
    CircularDoublyLinkedList,
)

linked_list_data = [3, 23.234, -21.3, "e", False, tuple]


def test_linked_list():
    # general test
    linked_list = LinkedList()
    linked_list.append(linked_list_data)
    assert linked_list.head.data == linked_list_data[0]
    assert linked_list.head.next.data == linked_list_data[1]
    assert list(linked_list) == linked_list_data
    assert str(linked_list) == linked_list_data.__str__()
    assert len(linked_list) == len(linked_list_data)

    # test insert
    linked_list.insert(2, 4)
    linked_list.insert(0, "23")
    linked_list.insert(-1, True)
    assert list(linked_list) == ["23", 3, 23.234, 4, -21.3, "e", False, tuple, True]
    assert len(linked_list) == 9

    # test delete
    linked_list.delete(3)
    linked_list.delete(tuple)
    linked_list.delete(1212)
    assert list(linked_list) == ["23", 23.234, 4, -21.3, "e", False, True]
    assert len(linked_list) == len(linked_list_data) + 1

    # test empty
    another_ll = LinkedList()
    assert another_ll.head.data is None
    assert list(another_ll) == []

    # test edge case
    a = LinkedList()
    a.append_left(1)
    assert a.head.data == 1
    a.delete(1)
    a.delete(1)
    assert a.head.data == None

    # test append
    another_ll.append(3)
    another_ll.append(2)
    another_ll.append(8.7)
    another_ll.append_left([1.2, 3])
    another_ll.append_left(-8.8)
    assert another_ll.head.data == -8.8
    assert len(another_ll) == 6

    # test_reverse
    another_ll.reverse()
    assert list(another_ll) == [8.7, 2, 3, 3, 1.2, -8.8]


def test_doubly_linked_list():
    # general test
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(linked_list_data)
    assert doubly_linked_list.head.data == linked_list_data[0]
    assert doubly_linked_list.head.next.data == linked_list_data[1]
    assert list(doubly_linked_list) == linked_list_data
    assert str(doubly_linked_list) == linked_list_data.__str__()
    assert len(doubly_linked_list) == len(linked_list_data)

    # test insert
    doubly_linked_list.insert(2, 4)
    doubly_linked_list.insert(0, "23")
    doubly_linked_list.insert(-1, True)
    assert list(doubly_linked_list) == [
        "23",
        3,
        23.234,
        4,
        -21.3,
        "e",
        False,
        tuple,
        True,
    ]
    assert len(doubly_linked_list) == 9
    assert doubly_linked_list.tail.prev.data == tuple
    assert doubly_linked_list.head.next.data == 3

    # test delete
    doubly_linked_list.delete(3)
    doubly_linked_list.delete(tuple)
    doubly_linked_list.delete(1212)
    doubly_linked_list.delete(True)
    doubly_linked_list.delete("23")
    assert list(doubly_linked_list) == [23.234, 4, -21.3, "e", False]
    assert len(doubly_linked_list) == len(linked_list_data) - 1
    assert doubly_linked_list.tail.prev.data == "e"
    assert doubly_linked_list.head.next.data == 4

    # test empty
    another_dll = DoublyLinkedList()
    another_dll.delete(3)
    assert another_dll.head.data is None
    assert list(another_dll) == []

    # test edge case
    a = DoublyLinkedList()
    a.append_left(1)
    assert a.head.data == a.tail.data == 1
    a.delete(1)
    a.delete(1)
    assert a.head.data == a.tail.data == None

    # test append
    another_dll.append(1)
    another_dll.append([4, 7])
    another_dll.append_left([44, 0])
    another_dll.append_left(12)
    assert another_dll.head.data == 12
    assert another_dll.tail.prev.data == 4
    assert list(another_dll) == [12, 44, 0, 1, 4, 7]
    assert len(another_dll) == 6

    # test reverse
    another_dll.reverse()
    assert list(another_dll) == [7, 4, 1, 0, 44, 12]
    assert another_dll.tail.prev.data == 44
    assert another_dll.head.next.data == 4


def test_circular_linked_list():
    # general test
    circular_linked_list = CircularLinkedList()
    circular_linked_list.append(linked_list_data)
    assert circular_linked_list.head.data == linked_list_data[0]
    assert circular_linked_list.head.next.data == linked_list_data[1]
    assert circular_linked_list.tail.next.data == linked_list_data[0]
    assert list(circular_linked_list) == linked_list_data
    assert str(circular_linked_list) == linked_list_data.__str__()
    assert len(circular_linked_list) == len(linked_list_data)

    # test delete
    circular_linked_list.delete("e")
    circular_linked_list.delete(124)
    circular_linked_list.delete(3)
    circular_linked_list.delete(23.234)
    assert list(circular_linked_list) == [-21.3, False, tuple]
    assert len(circular_linked_list) == 3
    assert circular_linked_list.tail.data == tuple
    assert circular_linked_list.tail.next == circular_linked_list.head

    # test empty
    another_cll = CircularLinkedList()
    another_cll.reverse()
    assert another_cll.head.data is None
    assert list(another_cll) == []

    # test edge case
    a = CircularLinkedList()
    a.append_left(1)
    assert a.head.data == 1
    a.delete(1)
    a.delete(1)
    assert a.head.data == a.tail.data == None
    a.insert(1142, 2)
    assert a.head.data == 2

    # test append
    another_cll.append(1)
    another_cll.append([4, 7])
    another_cll.append_left([44, 0])
    another_cll.append_left(12)
    assert another_cll.head.data == 12
    assert another_cll.tail.next.data == 12
    assert list(another_cll) == [12, 44, 0, 1, 4, 7]
    assert len(another_cll) == 6

    # test reverse
    another_cll.reverse()
    assert list(another_cll) == [7, 4, 1, 0, 44, 12]
    assert another_cll.tail.data == 12
    assert another_cll.tail.next == another_cll.head

    # test insert
    another_cll.insert(2, 4)
    another_cll.insert(0, "23")
    another_cll.insert(-1, True)
    assert list(another_cll) == ["23", 7, 4, 4, 1, 0, 44, 12, True]
    assert another_cll.head.data == another_cll.tail.next.data


def test_circular_doubly_linked_list():
    # general test
    circular_doubly_linked_list = CircularDoublyLinkedList()
    circular_doubly_linked_list.append(linked_list_data)
    assert circular_doubly_linked_list.head.data == linked_list_data[0]
    assert circular_doubly_linked_list.head.next.data == linked_list_data[1]
    assert circular_doubly_linked_list.tail.next.data == linked_list_data[0]
    assert list(circular_doubly_linked_list) == linked_list_data
    assert str(circular_doubly_linked_list) == linked_list_data.__str__()
    assert len(circular_doubly_linked_list) == len(linked_list_data)

    # test delete
    circular_doubly_linked_list.delete("e")
    circular_doubly_linked_list.delete(124)
    circular_doubly_linked_list.delete(3)
    circular_doubly_linked_list.delete(tuple)
    assert list(circular_doubly_linked_list) == [23.234, -21.3, False]
    assert len(circular_doubly_linked_list) == 3
    assert circular_doubly_linked_list.tail.data == False
    assert circular_doubly_linked_list.tail.next == circular_doubly_linked_list.head
    assert (
        circular_doubly_linked_list.head.prev.prev.data
        == circular_doubly_linked_list.tail.prev.data
    )

    # test empty
    another_cdll = CircularDoublyLinkedList()
    another_cdll.reverse()
    assert another_cdll.head.data is None
    assert list(another_cdll) == []

    # test edge case
    a = CircularDoublyLinkedList()
    a.append_left(1)
    assert a.head.data == a.tail.data == 1
    a.delete(1)
    a.delete(1)
    assert a.head.data == a.tail.data == None
    a.insert(1142, 2)
    assert a.head.data == 2

    # test append
    another_cdll.append(1)
    another_cdll.append([4, 7])
    another_cdll.append_left([44, 0])
    another_cdll.append_left(12)
    assert another_cdll.head.data == 12
    assert another_cdll.tail.next.data == 12
    assert (
        circular_doubly_linked_list.head.prev.prev.data
        == circular_doubly_linked_list.tail.prev.data
    )
    assert list(another_cdll) == [12, 44, 0, 1, 4, 7]
    assert len(another_cdll) == 6

    # test reverse
    another_cdll.reverse()
    assert list(another_cdll) == [7, 4, 1, 0, 44, 12]
    assert another_cdll.tail.data == 12
    assert another_cdll.tail.next == another_cdll.head
    assert (
        circular_doubly_linked_list.head.prev.prev.data
        == circular_doubly_linked_list.tail.prev.data
    )

    # test insert
    another_cdll.insert(2, 4)
    another_cdll.insert(0, "23")
    another_cdll.insert(-1, True)
    assert list(another_cdll) == ["23", 7, 4, 4, 1, 0, 44, 12, True]
    assert another_cdll.head.data == another_cdll.tail.next.data
    assert (
        circular_doubly_linked_list.head.prev.prev.data
        == circular_doubly_linked_list.tail.prev.data
    )


"""
if __name__ == "__main__":
    import pytest
    pytest.main()
"""
