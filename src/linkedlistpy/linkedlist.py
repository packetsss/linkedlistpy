from typing import Any, Union, List, Set, Dict, Tuple, Optional, Sequence, Iterable


# Represents the node of list.
class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self) -> None:
        self.head = Node(None)
        self._length = 0
    
    def __len__(self) -> int:
        return self._length
        
    def __iter__(self) -> Iterable[Any]:
        current = self.head
        if current.data is None:
            return iter([])

        output_list = []
        while current:
            output_list.append(current.data)
            current = current.next

        return iter(output_list)

    def __repr__(self) -> str:
        return list(self.__iter__()).__repr__()

    def append(self, data: Any) -> None:
        if not isinstance(data, Iterable):
            data = [data]
        for d in data:
            new_node = Node(d)
            self._length += 1
            if self.head.data is None:
                self.head = new_node
                continue
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node
            

    def append_left(self, data: Any) -> None:
        if not isinstance(data, Iterable):
            data = [data]

        data = reversed(data)
        for d in data:
            new_node = Node(d)
            new_node.next = self.head
            self.head = new_node
            self._length += 1

    def delete(self, value: Any) -> None:
        temp = self.head

        if temp.data is not None:
            if temp.data == value:
                self.head = temp.next
                temp = None
                self._length -= 1
                return
        while temp is not None:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return

        prev.next = temp.next
        temp = None
        self._length -= 1

    def reverse(self) -> None:
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head
        self._length = 0

    def __len__(self) -> int:
        return self._length
    
    def __iter__(self) -> Iterable[Any]:
        current = self.head
        if current.data is None:
            return iter([])
        output_list = [current.data]
        while current.next is not None and current.next != self.head:
            current = current.next
            output_list.append(current.data)
        return iter(output_list)

    def __repr__(self) -> str:
        return list(self.__iter__()).__repr__()

    def append(self, data: Any) -> None:
        if not isinstance(data, Iterable):
            data = [data]
        for d in data:
            new_node = Node(d)
            if self.head.data is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = self.head
            else:
                self.tail.next = new_node
                self.tail = new_node
                self.tail.next = self.head
            self._length += 1

    def append_left(self, data: Any) -> None:
        if not isinstance(data, Iterable):
            data = [data]

        data = reversed(data)
        for d in data:
            new_node = Node(d)
            if self.head.data is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = self.head
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head
            self._length += 1

    def delete(self, value: Any) -> None:
        current = self.head
        prev = None
        while True:
            # found
            if current.data == value:
                if prev is not None:
                    prev.next = current.next
                else:
                    while current.next != self.head:
                        current = current.next
                    current.next = self.head.next
                    self.head = self.head.next
                self._length -= 1
                return
            # not found
            elif current.next == self.head:
                return
            prev = current
            current = current.next


    def reverse(self) -> None:
        head_ref = self.head
        if head_ref.data is None:
            return

        prev = None
        current = head_ref
        next = current.next
        current.next = prev
        prev = current
        current = next
        while current != head_ref:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head.next = prev
        self.head = prev
        curr = self.head
        while curr.next is not None and curr.next != self.head:
            curr = curr.next
        self.tail = curr
