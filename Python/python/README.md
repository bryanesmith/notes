# Python

## Assertions

* Signal unrecoverable errors
* E.g., the following shape errors would be unrecoverable:
    ```python
    assert y.shape == (20,)
    assert X.shape == (20,1)
    assert np.isscalar(b)
    ```

## Classes

```py
class MyClass:
    number = 17     # class attr
    string = "hi!"  # class attr

obj = MyClass()
obj.number 
```

* **dunder method**: **d**ouble **under**score **method**

```py
class MyClass:
    counter = 0             # class attr

    def __init__(self, loc):
        self.x = loc[0]     # instance attr
        self.y = loc[1]     # instance attr
    
    def increment_counter(self):
        MyClass.counter += 1    

obj = MyClass((1,2))
obj.x 
obj.increment_counter()
obj.counter
```

* Special methods:
    - `__init__`
    - `__str__`
    - `__eq__` and `__ne__`
    - `__hash__`
    - `ininstance(obj, SomeClass)`
    - `type(obj)` # some class

* Inheritance:
    ```py
    class Polygon:
        def __init__(self, side_count):
            self.side_count = side_count
    
    class Triangle(Polygon):
        def __init__(self):
            super().__init__(3)
        def __str__(self):
            return f'A triangle has {self.side_count} sides'
    ```

* Abstract classes using the **Abstract Base Class** module in Python:
    ```py
    from abc import ABC, abstractmethod, abstractproperty

    class Animal(ABC):

        def breath(self):
            print('Takes a breath')

        @abstractmethod
        def move(self):
            pass

        @abstractproperty
        def arm_count(self):
            pass
    
    class Human(Animal):

        def __init__(self, name):
            self.name = name
        
        def move(self):
            print("Walks on 2 legs")
        
        @property
        def arm_count(self):
            return 2
    
    cj = Human('CJ Abrams')
    cj.name
    cj.move()
    cj.arm_count
    ```

* Class mixins:
    ```py
    class FlyingMixin:
        def fly(self):
            print("I'm flying")
    
    class Bird:
        def chirp(self):
            print("Chirp chirp!")
    
    class Parrot(Bird, FlyingMixin):
        pass
    ```

## Dicts

* Mutable
* Keys must be **hashable**, meaning muts be immutable
* Constructing dicts:
    - `dict([('key1', 'value1'), ('key2', 'value2')])`
    - `dict(key1='value1', key2='value2')`
    - Literals: `{'key1': 'value1'}`
    - `dict.fromkeys(['key1', 'key2'], default_val)`
* Accessing:
    - `a_dict['key']` is not safe (results in `KeyError` if key not found)
    - `a_dict.get('key', default_obj)` is safe
* Looping
    - `for key in a_dict:`
    - `for key, value in a_dict.items():`
* Since 3.7, dicts are ordered; since 3.8, dicts are reversible using `reversed(...)`
* Useful methods:
    - Removing: `del a_dict[key]` and `a_dict.pop(key)` not safe (`KeyError`), `a_dict.pop(key, default_val)` safe
    - Get and set if not present: `a_dict.setdefault('key', some_val)`
    - `a_dict.keys()`, `a_dict.values()`
    - Can't sort dicts, but can create sorted views: `dict(sorted(a_dict.items()))`
    - Merging: `dict_1.update(dict_2)` or `dict_1 |= dict_2` (destructive), `dict_1 | dict_2` (non-destructive)

## Enums

```python
from enum import Enum 

class Coin(Enum):
    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUARTER = 25

def change_due(value_in_cents: int) -> dict[Coin, int]:
    change = {}
    for coin_type in [Coin.QUARTER, Coin.DIME, Coin.NICKEL, Coin.PENNY]:
        change[coin_type] = int(value_in_cents / coin_type.value)
        value_in_cents %= coin_type.value
    return change
```

## Exceptions

```python
import sys

try:
    f = open(file)
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
```

```python
raise Exception("Hello, world")

raise NameError("Goodbye, cruel world")

raise KeyboardInterrupt # Without arguments

raise # re-raises an exception
```

## Files

### Globbing

```python
import glob

files = glob.glob("data/*.csv")
```

### Paths

```python
from os import path

if path.exists(file):
    process(file)
```

### Reading file

```python
with open(file, 'r') as reader:
    next(reader) # Skip line
    for line in reader: # Read remaining lines
        print(line)
```

### Writing file

```python
with open(file, 'w') as writer:
    writer.write(str) # Doesn't automatically add newline
```

## Generators

* A **generator** is a function/expression that returns a special type of iterator called a **generator iterator**
    - Generator iterators are **lazy**, meaning do not store values in memory, but are generated on demand
    - These iterators contain `yield`

```py
# finite
def powers(numbers, power):
    for num in numbers:
        yield num ** power

gen = powers([1, 2, 3, 4, 5], 2)
for val in gen:
    print(val) # 1 4 9 16 25
```

* Can access values using `next(some_generator)`, which calls the `__next__()` method on the object
    - When generator is fully consumed, calling `next` will raise a `StopIteration`
* Generators are one-way; cannot revisit previous values
* Generators cannot be reversed or sorted
* Generators cannot use `len(generator)`

```py
def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_counter()
next(gen)
next(gen)
next(gen)
```

## Lambdas

```python
import numpy as np
a = np.fromfunction(lambda x, y: 10*x+y, (5,4), dtype=int)
# a = array([[ 0,  1,  2,  3],
#            [10, 11, 12, 13],
#            [20, 21, 22, 23],
#            [30, 31, 32, 33],
#            [40, 41, 42, 43]])
```

## Lists

* Mutable, implemented as **dynamic arrays** (similar to Java's `ArrayList`)
    - Prepending or inserting into middle of list inefficient as must shift elements
* Convert another collection to list using `list(("a", "b", "c"))` or `[*('a', 'b', 'c')]`
    - `[17]` works, but `list(17)` because `list` method only accepts iterables
* **Slicing**. E.g., `list[2:]`
* To create an 8x8 matrix of zeros: `[[0] * 8] * 8`
* Commonly used methods:
    - Adding elements: `list.append(some_obj)`, `list.insert(index, some_obj)`
    - Removing elements: `list.remove(some_obj)`, `list.pop(index)`, `list.clear()`
    - Finding: `some_obj in list`, `list.index(some_obj)`, `list.count(some_obj)`
    - Shallow copy: `list.copy()`
    - Concatenate lists: `list_1 + list_2` (non-destructive), `list_1.extend(list_2)` (destructive)
    - Sorting: `sorted(list)` (non-destructive), `list.sort()` (destructive), `list.sort(reverse=True)`
    - `list.reverse()`
    - `min(list)`, `max(list)`

## List comprehensions

```python
x = [i for i in range(5)]
# [0, 1, 2, 3, 4]

y = [y for y in range(10) if y%2==0]
# [0, 2, 4, 6, 8]

z = [x.int() for x in "testing 123" if x.isdigit()]
# [1, 2, 3]
```

## Regular expressions

* If found:
    ```python
    # Find any non-numeric characters
    p = r"[^0-9]"

    # Same as:
    #pattern = "[^0-9]"
    #p = re.compile(pattern) 

    input = '856961Z503833437' # note contains a 'Z'
    if re.search(p, input):
        print('Found a non-numeric character')
    ```

* Find captured values:
    ```python
    import re

    # Find dates in files with name: mm-dd-yyyy.csv
    pattern = r"(\d{2}-\d{2}-\d{4}).csv"
    dates = [re.findall(pattern, f)[0] for f in files if re.search(pattern, f)]
    ```

* Replace:
    ```python
    import re
    re.sub(r'\s', '', "He\tllo, \n World!" )
    ```

## Sets

* Mutable and unordered collection
    - Not permitted: indexing, slicing, contatenation with `+`
* Duplicate items are ignored
* Construction:
    - Literals: `{ obj_1 }`
    - Constructor: `set(an_iterable)`
    - Note: `{'abc'}` -> `{'abc'}`, but `set('abc')` -> `{'b', 'a', 'c'}`
* All set elements must be hashable, meaning they must be immutable (e.g., sets can't hold lists, other sets, dicts, etc)
* Useful methods:
    - Add: `a_set.add(some_obj)`
    - Iteration: `for item in a_set:`
    - Membership: `item in a_set`, `item not in a_set`
    - `len(a_set)`
    - `a_set.copy()`
    - Disjoint: `set_1.isdisjoint(coll_2)`
    - Subsets: `set_1.issubset(coll_2)`, `set_1 <= set_2`
    - Superset: `set_1.issuperset(coll_2)`, `set_1 >= set_2`
    - Intersection: `set_1.intersection(iterable_2)`, `set_1 & set_2`
    - Union: `set_1.union(set_2)`, `set_1 | set_2`
    - Difference: `set_1.difference(iterable_2)`, `set_1 - set_2`
    - "Symmetric difference" returns elects in either but not both sets: `set_1.symmetric_difference(iterable_2)`, `set_1 ^ set_2`

## Strings

* Immutable
* Iterable using `for item in str:` or `for index, item in enumerate(str):`
* `List(str)` or `[*str]` to convert a string to a list of characters
* Commonly used methods:
    - Testing: `str.startswith(substr)`, `str.endswith(substr)`
    - Casing: `str.title()`, `str.upper()`, `str.lower()`, `str.swapcase()`
    - Removing or replacing: `str.strip(chars)`, `str.lstrip(chars)`, `str.rstrip(chars)`, `str.removeprefix(substr)`, `str.removesuffic(substr)`, `str.replace(old, new)`

## Ternary Operator

```python
min = a if a < b else b 
```

## Tuples

* Immutable
* Constructed using `()` literal or `tuple(some_collection)`
* Supports same indexing and slicing as lists

## Type hints

```python
from typing import List

def load_data(file_name: str) -> List[str]:
    pass
```

## Examples

* [collate_covid19_daily_observation_summaries.py](collate_covid19_daily_observation_summaries.py): regex, globbing, file I/O, type hints, list comprehensions.
