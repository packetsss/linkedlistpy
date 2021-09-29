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
    linked_list_3 = LinkedList()
    assert linked_list_3.head.data is None
    assert list(linked_list_3) == []

    # test edge case
    linked_list_2 = LinkedList()
    linked_list_2.append_left(1)
    assert linked_list_2.head.data == 1
    linked_list_2.delete(1)
    linked_list_2.delete(1)
    assert linked_list_2.head.data == None

    # test append
    linked_list_3.append(3)
    linked_list_3.append(2)
    linked_list_3.append(8.7)
    linked_list_3.append_left([1.2, 3])
    linked_list_3.append_left(-8.8)
    assert linked_list_3.head.data == -8.8
    assert len(linked_list_3) == 6

    # test_reverse
    linked_list_3.reverse()
    assert list(linked_list_3) == [8.7, 2, 3, 3, 1.2, -8.8]


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
    doubly_linked_list_3 = DoublyLinkedList()
    doubly_linked_list_3.delete(3)
    assert doubly_linked_list_3.head.data is None
    assert list(doubly_linked_list_3) == []

    # test edge case
    doubly_linked_list_2 = DoublyLinkedList()
    doubly_linked_list_2.append_left(1)
    assert doubly_linked_list_2.head.data == doubly_linked_list_2.tail.data == 1
    doubly_linked_list_2.delete(1)
    doubly_linked_list_2.delete(1)
    assert doubly_linked_list_2.head.data == doubly_linked_list_2.tail.data == None

    # test append
    doubly_linked_list_3.append(1)
    doubly_linked_list_3.append([4, 7])
    doubly_linked_list_3.append_left([44, 0])
    doubly_linked_list_3.append_left(12)
    assert doubly_linked_list_3.head.data == 12
    assert doubly_linked_list_3.tail.prev.data == 4
    assert list(doubly_linked_list_3) == [12, 44, 0, 1, 4, 7]
    assert len(doubly_linked_list_3) == 6

    # test reverse
    doubly_linked_list_3.reverse()
    assert list(doubly_linked_list_3) == [7, 4, 1, 0, 44, 12]
    assert doubly_linked_list_3.tail.prev.data == 44
    assert doubly_linked_list_3.head.next.data == 4


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
    circular_linked_list_3 = CircularLinkedList()
    circular_linked_list_3.reverse()
    assert circular_linked_list_3.head.data is None
    assert list(circular_linked_list_3) == []

    # test edge case
    circular_linked_list_2 = CircularLinkedList()
    circular_linked_list_2.append_left(1)
    assert circular_linked_list_2.head.data == 1
    circular_linked_list_2.delete(1)
    circular_linked_list_2.delete(1)
    assert circular_linked_list_2.head.data == circular_linked_list_2.tail.data == None
    circular_linked_list_2.insert(1142, 2)
    assert circular_linked_list_2.head.data == 2

    # test append
    circular_linked_list_3.append(1)
    circular_linked_list_3.append([4, 7])
    circular_linked_list_3.append_left([44, 0])
    circular_linked_list_3.append_left(12)
    assert circular_linked_list_3.head.data == 12
    assert circular_linked_list_3.tail.next.data == 12
    assert list(circular_linked_list_3) == [12, 44, 0, 1, 4, 7]
    assert len(circular_linked_list_3) == 6

    # test reverse
    circular_linked_list_3.reverse()
    assert list(circular_linked_list_3) == [7, 4, 1, 0, 44, 12]
    assert circular_linked_list_3.tail.data == 12
    assert circular_linked_list_3.tail.next == circular_linked_list_3.head

    # test insert
    circular_linked_list_3.insert(2, 4)
    circular_linked_list_3.insert(0, "23")
    circular_linked_list_3.insert(-1, True)
    assert list(circular_linked_list_3) == ["23", 7, 4, 4, 1, 0, 44, 12, True]
    assert circular_linked_list_3.head.data == circular_linked_list_3.tail.next.data


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
    circular_doubly_linked_list_3 = CircularDoublyLinkedList()
    circular_doubly_linked_list_3.reverse()
    assert circular_doubly_linked_list_3.head.data is None
    assert list(circular_doubly_linked_list_3) == []

    # test edge case
    circular_doubly_linked_list_2 = CircularDoublyLinkedList()
    circular_doubly_linked_list_2.append_left(1)
    assert circular_doubly_linked_list_2.head.data == circular_doubly_linked_list_2.tail.data == 1
    circular_doubly_linked_list_2.delete(1)
    circular_doubly_linked_list_2.delete(1)
    assert circular_doubly_linked_list_2.head.data == circular_doubly_linked_list_2.tail.data == None
    circular_doubly_linked_list_2.insert(1142, 2)
    assert circular_doubly_linked_list_2.head.data == 2

    # test append
    circular_doubly_linked_list_3.append(1)
    circular_doubly_linked_list_3.append([4, 7])
    circular_doubly_linked_list_3.append_left([44, 0])
    circular_doubly_linked_list_3.append_left(12)
    assert circular_doubly_linked_list_3.head.data == 12
    assert circular_doubly_linked_list_3.tail.next.data == 12
    assert (
        circular_doubly_linked_list.head.prev.prev.data
        == circular_doubly_linked_list.tail.prev.data
    )
    assert list(circular_doubly_linked_list_3) == [12, 44, 0, 1, 4, 7]
    assert len(circular_doubly_linked_list_3) == 6

    # test reverse
    circular_doubly_linked_list_3.reverse()
    assert list(circular_doubly_linked_list_3) == [7, 4, 1, 0, 44, 12]
    assert circular_doubly_linked_list_3.tail.data == 12
    assert circular_doubly_linked_list_3.tail.next == circular_doubly_linked_list_3.head
    assert (
        circular_doubly_linked_list.head.prev.prev.data
        == circular_doubly_linked_list.tail.prev.data
    )

    # test insert
    circular_doubly_linked_list_3.insert(2, 4)
    circular_doubly_linked_list_3.insert(0, "23")
    circular_doubly_linked_list_3.insert(-1, True)
    assert list(circular_doubly_linked_list_3) == ["23", 7, 4, 4, 1, 0, 44, 12, True]
    assert circular_doubly_linked_list_3.head.data == circular_doubly_linked_list_3.tail.next.data
    assert (
        circular_doubly_linked_list.head.prev.prev.data
        == circular_doubly_linked_list.tail.prev.data
    )


"""
if __name__ == "__main__":
    import pytest
    pytest.main()
"""
