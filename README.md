# pylinkedlist - a Linked List library
**This library provides linked lists so that you won't have to build your own! (especially for those evil interviews)**

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/packetsss/linkedlistpy/Tests?style=for-the-badge)](https://github.com/packetsss/linkedlistpy/actions) [![pypi](https://shields.io/pypi/v/linkedlistpy?style=for-the-badge)](https://pypi.org/project/linkedlistpy/) [![GitHub stars](https://img.shields.io/github/stars/packetsss/linkedlistpy?style=for-the-badge)](https://github.com/packetsss/linkedlistpy/stargazers)


## Installation
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
- insert
- delete
- reverse
