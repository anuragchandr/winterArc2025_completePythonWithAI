# DAY3

## List

- Declaration : ```name = ["value1", "value2", "value3"]```
- Lists are:
  - mutable
  - ordered
  - allow duplicate items
  - indexable (starting from 0)
  - can store mixed data types

### Common List Methods

- `append(item)` : Adds an item to the end of the list.
- `extend(iterable)` : Adds elements from another iterable.
- `insert(index, item)` : Inserts an item at a specific index.
- `remove(item)` : Removes the first occurrence of the item.
- `pop(index)` : Removes and returns item at index (default last).
- `clear()` : Removes all items from the list.
- `index(item)` : Returns the index of the first occurrence.
- `count(item)` : Counts how many times an item appears.
- `sort()` : Sorts the list in ascending order.
- `reverse()` : Reverses the order of the list.
- `copy()` : Returns a shallow copy of the list.

## Tuple

- Declaration : ```name = ("value1", "value2", "value3")```
- Tuples are:
  - immutable
  - ordered
  - allow duplicate items
  - indexable (starting from 0)
  - faster than lists for fixed data

### Common Tuple Methods

- `count(item)` : Returns the number of times an item appears.
- `index(item)` : Returns the index of the first occurrence.
