from typing import Any, Union, List, Set, Dict, Tuple, Optional, Sequence, Iterable


# Represents the node of list.
class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class LinkedList:
    def __init__(self) -> None:
        self.head = Node(None)
        self._length = 0

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> Iterable[Any]:
        curr = self.head
        if curr.data is None:
            return iter([])

        output_list = []
        while curr:
            output_list.append(curr.data)
            curr = curr.next

        return iter(output_list)

    def __repr__(self) -> str:
        return list(self.__iter__()).__repr__()

    def append(self, data: Any) -> None:
        if not isinstance(data, Iterable) or isinstance(data, str):
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
        if not isinstance(data, Iterable) or isinstance(data, str):
            data = [data]

        data = reversed(data)
        for d in data:
            new_node = Node(d)
            new_node.next = self.head
            self.head = new_node
            self._length += 1

    def insert(self, index: int, value: Any) -> None:
        index = max(-self._length, min(index, self._length))
        if index == 0:
            self.append_left(value)
            return
        elif index < 0:
            index = self._length + index + 1

        curr = self.head
        new_node = Node(value)
        for _ in range(index - 1):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        self._length += 1

    def delete(self, value: Any) -> None:
        if self.head.data is None:
            return

        temp = self.head
        prev = None
        while temp is not None:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        if prev is None and self._length == 1:
            self.head = Node(None)
        else:
            prev.next = temp.next
            temp = None
        self._length -= 1

    def reverse(self) -> None:
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self._length = 0

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> Iterable[Any]:
        curr = self.head
        if curr.data is None:
            return iter([])

        output_list = []
        while curr:
            output_list.append(curr.data)
            curr = curr.next

        return iter(output_list)

    def __repr__(self) -> str:
        return list(self.__iter__()).__repr__()

    def append(self, data: Any) -> None:
        if not isinstance(data, Iterable) or isinstance(data, str):
            data = [data]
        for d in data:
            new_node = Node(d)
            if not self.head.data:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            self._length += 1

    def append_left(self, data: Any) -> None:
        if not isinstance(data, Iterable) or isinstance(data, str):
            data = [data]

        data = reversed(data)
        for d in data:
            new_node = Node(d)
            if not self.tail.data:
                print(1)
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
                print(self.head.data)
            self._length += 1

    def insert(self, index: int, value: Any) -> None:
        index = max(-self._length, min(index, self._length))
        if index == 0:
            self.append_left(value)
            return
        elif index < 0:
            index = self._length + index + 1
        if index == self._length:
            self.append(value)
            return

        curr = self.head
        new_node = Node(value)
        for _ in range(index - 1):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        new_node.prev = curr
        self._length += 1

    def delete(self, value: Any) -> None:
        if self.head.data is None:
            return

        curr = self.head
        if curr.data == value:
            if self._length == 1:
                self.head = Node(None)
                self.tail = Node(None)
            else:
                self.head = curr.next
                self.head.prev = None
        elif self.tail.data == value:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            while curr:
                if curr.data == value:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    break
                curr = curr.next
            else:
                return
        self._length -= 1

    def reverse(self):
        # Node curr will point to head
        curr = self.head

        # Swap the prev and next pointers of each node to reverse the direction of the list
        while curr != None:
            temp = curr.next
            curr.next = curr.prev
            curr.prev = temp
            curr = curr.prev

        # Swap the head and tail pointers.
        temp = self.head
        self.head = self.tail
        self.tail = temp


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = Node(None)
        self.tail = Node(None)
        self._length = 0

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> Iterable[Any]:
        curr = self.head
        if curr.data is None:
            return iter([])
        output_list = [curr.data]
        while curr.next is not None and curr.next != self.head:
            curr = curr.next
            output_list.append(curr.data)
        return iter(output_list)

    def __repr__(self) -> str:
        return list(self.__iter__()).__repr__()

    def append(self, data: Any) -> None:
        if not isinstance(data, Iterable) or isinstance(data, str):
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
        if not isinstance(data, Iterable) or isinstance(data, str):
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

    def insert(self, index: int, value: Any) -> None:
        index = max(-self._length, min(index, self._length))
        if index == 0:
            self.append_left(value)
            return
        elif index < 0:
            index = self._length + index + 1
        if index >= self._length:
            self.append(value)
            return

        curr = self.head
        new_node = Node(value)
        for _ in range(index - 1):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        self._length += 1

    def delete(self, value: Any) -> None:
        if self.head.data is None:
            return
        curr = self.head
        prev = None
        while 1:
            # found
            if curr.data == value:
                if self._length == 1:
                    self.head = Node(None)
                    self.tail = Node(None)
                elif prev is not None:
                    prev.next = curr.next
                else:
                    while curr.next != self.head:
                        curr = curr.next
                    curr.next = self.head.next
                    self.head = self.head.next
                self._length -= 1
                return
            # not found
            elif curr.next == self.head:
                return
            prev = curr
            curr = curr.next

    def reverse(self) -> None:
        head_ref = self.head
        if head_ref.data is None:
            return

        prev = None
        curr = head_ref
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        while curr != head_ref:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head.next = prev
        self.head = prev
        curr = self.head
        while curr.next is not None and curr.next != self.head:
            curr = curr.next
        self.tail = curr


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self._length = 0

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> Iterable[Any]:
        curr = self.head
        if curr.data is None:
            return iter([])
        output_list = [curr.data]
        while curr.next is not None and curr.next != self.head:
            curr = curr.next
            output_list.append(curr.data)
        return iter(output_list)

    def __repr__(self) -> str:
        return list(self.__iter__()).__repr__()

    def append(self, data: Any) -> None:
        if not isinstance(data, Iterable) or isinstance(data, str):
            data = [data]

        for d in data:
            if self.head.data is None:
                self.head = Node(d)
                self.tail = self.head
                self.tail.next = self.head
                self.head.prev = self.tail
            else:
                new_node = Node(d)
                self.tail.next = new_node
                new_node.prev = self.tail
                new_node.next = self.head
                self.head.prev = new_node
                self.tail = self.tail.next
            self._length += 1

    def append_left(self, data: Any) -> None:
        if not isinstance(data, Iterable) or isinstance(data, str):
            data = [data]

        data = reversed(data)
        for d in data:
            if self.head.data is None:
                self.head = Node(d)
                self.tail = self.head
                self.tail.next = self.head
                self.head.prev = self.tail
            else:
                new_node = Node(d)
                new_node.next = self.head
                self.head.prev = new_node
                self.tail.next = new_node
                new_node.prev = self.tail
                self.head = self.head.prev
            self._length += 1

    def insert(self, index: int, value: Any) -> None:
        index = max(-self._length, min(index, self._length))
        if index == 0:
            self.append_left(value)
            return
        elif index < 0:
            index = self._length + index + 1
        if index >= self._length:
            self.append(value)
            return

        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        new_node = Node(value)
        curr.next.prev = new_node
        new_node.next = curr.next
        new_node.prev = curr
        curr.next = new_node
        return

    def delete(self, value):
        if self.head.data is None:
            return

        if self.head.data == value:
            if self._length == 1:
                self.head = Node(None)
                self.tail = Node(None)
            else:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                if curr.data == value:
                    break
                curr = curr.next
            else:
                if curr.data == value:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                    self._length -= 1
                return

            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        self._length -= 1

    def reverse(self):
        self.head, self.tail = self.tail, self.head
        start = curr = self.head
        if curr is not None:
            curr.next, curr.prev = curr.prev, curr.next
            curr = curr.prev
        while curr is not None and curr is not start:
            curr.next, curr.prev = curr.prev, curr.next
            curr = curr.prev  # move to the next node
