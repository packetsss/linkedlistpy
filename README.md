# pylinkedlist - A TYPED Linked List Library
**This library provides all types of linked lists so that you won't have to implement your own! (especially for those evil interviews)**

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
linked_list.append_left([3, "foo", tuple, True])
print(linked_list)
>> [3, 'foo', <class 'tuple'>, True, 1]

print(len(linked_list))
>> 5

print(list(linked_list), type(str(linked_list)))
>> [3, 'foo', <class 'tuple'>, True, 1] <class 'str'>

linked_list.reverse()
print(linked_list)
>> [1, True, <class 'tuple'>, 'foo', 3]

linked_list.insert(3, "bar")
print(linked_list)
>> [1, True, <class 'tuple'>, 'bar', 'foo', 3]

linked_list.delete(tuple)
print(linked_list)
>> [1, True, 'bar', 'foo', 3]

```


## Features included (for now)

### Linked Lists
- Singly Linked list
- Doubly Linked list
- Circular Linked list
- Circular Doubly Linked list

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
