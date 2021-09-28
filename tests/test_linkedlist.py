import pytest
from linkedlistpy import LinkedList, CircularLinkedList

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

    # test delete
    linked_list.delete(3)
    linked_list.delete(tuple)
    linked_list.delete(1212)
    assert list(linked_list) == linked_list_data[1:-1]
    assert len(linked_list) == len(linked_list_data) - 2

    # test empty
    another_ll = LinkedList()
    assert another_ll.head.data is None
    assert list(another_ll) == []

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


another_cll = CircularLinkedList()
another_cll.append([1, 4, 7])
another_cll.append_left([12, 44, 0])
print(another_cll)
another_cll.reverse()
print(another_cll)


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
    assert list(circular_linked_list) == [23.234, -21.3, False, tuple]
    assert len(circular_linked_list) == 4
    assert circular_linked_list.tail.data == tuple
    assert circular_linked_list.tail.next == circular_linked_list.head
    
    # test empty
    another_cll = CircularLinkedList()
    another_cll.reverse()
    assert another_cll.head.data is None
    assert list(another_cll) == []

    # test append
    CircularLinkedList().append_left(1)
    another_cll.append(1)
    another_cll.append([4, 7])
    another_cll.append_left([44, 0])
    another_cll.append_left(12)
    assert another_cll.head.data == 12
    assert another_cll.tail.next.data == 12
    assert list(another_cll) == [12, 44, 0, 1, 4, 7]
    assert len(another_cll) == 6

    # test_reverse
    another_cll.reverse()
    assert list(another_cll) == [7, 4, 1, 0, 44, 12]
    assert another_cll.tail.data == 12
    assert another_cll.tail.next == another_cll.head


"""
if __name__ == "__main__":
    pytest.main()

"""
