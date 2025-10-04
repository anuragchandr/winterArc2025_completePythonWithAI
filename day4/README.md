# DAY 4

## Dictionary

- Declaration : ```name = {"key1": "value1", "key2": "value2"}```
- Dictionaries are:
  - mutable
  - ordered (Python 3.7+)
  - do not allow duplicate keys
  - store key-value pairs
  - fast for lookups via keys

### Common Dictionary Methods

- `get(key)` : Returns the value for the specified key.
- `keys()` : Returns a view of all keys.
- `values()` : Returns a view of all values.
- `items()` : Returns a view of key-value pairs.
- `update(other_dict)` : Updates with another dictionary.
- `pop(key)` : Removes and returns the value for the key.
- `clear()` : Removes all items.
- `copy()` : Returns a shallow copy.

## Set

- Declaration : ```name = {"value1", "value2", "value3"}```
- Sets are:
  - mutable
  - unordered
  - do not allow duplicate items
  - unindexed
  - useful for membership tests and unique collections

### Common Set Methods

- `add(item)` : Adds an item to the set.
- `remove(item)` : Removes the item (raises error if not found).
- `discard(item)` : Removes the item (no error if not found).
- `pop()` : Removes and returns a random item.
- `clear()` : Removes all items.
- `union(other_set)` : Returns a new set with all items.
- `intersection(other_set)` : Returns common items.
- `difference(other_set)` : Returns items not in the other set.
