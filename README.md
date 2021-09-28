# pylinkedlist - a Linked List library
**This library provides linked lists so that you won't have to build your own! (especially for evil interviews)**

![Tests](https://github.com/packetsss/pylinkedlist/actions/workflows/tests.yml/badge.svg)


## Install package
```
pip install linkedlistpy
```

## Quick start
```
from linkedlistpy import LinkedList

linked_list = LinkedList()

linked_list.append(1)
linked_list.append_left([3, "foo", tuple, true])

print(linked_list)
>> [3, "foo", tuple, true, 1]

linked_list.reverse()

print(linked_list)
>> [1, true, tuple, "foo", 3]
```





## Features included (for now)

### Linked Lists
- Singly Linked list
- Doubly Linked list (TODO)
- Circular Linked list
- Doubly Circular Linked list (TODO)

### Methods
- built-in
  - str
  - list
  - len
- append
- append_left
- delete
- reverse
