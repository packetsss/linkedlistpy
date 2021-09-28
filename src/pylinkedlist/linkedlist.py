from typing import Any, Union, List, Set, Dict, Tuple, Optional, Sequence, Iterable


# Represents the node of list.
class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional[Node] = None


class CircularLinkedList:
    # Declaring head and tail pointer as null.
    def __init__(self) -> None:
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

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
        # current: Node = self.head
        # if current.data is None:
        #     return "[]"

        # output_str = f"[{current.data}"
        # while current.next is not None and current.next != self.head:
        #     current = current.next
        #     output_str += f", {current.data}"
        # return f"{output_str}]"
        return list(self.__iter__()).__repr__()

    # This function will add the new node at the end of the list.
    def add(self, data: Any) -> None:
        if not isinstance(data, Iterable):
            data = [data]
        for d in data:
            new_node = Node(d)
            # Checks if the list is empty.
            if self.head.data is None:
                # If list is empty, both head and tail would point to new node.
                self.head = new_node
                self.tail = new_node
                new_node.next = self.head
            else:
                # tail will point to new node.
                self.tail.next = new_node
                # New node will become new tail.
                self.tail = new_node
                # Since, it is circular linked list tail will point to head.
                self.tail.next = self.head
