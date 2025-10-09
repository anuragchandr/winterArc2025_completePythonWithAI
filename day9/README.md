# DAY 9

## The `__init__` Method, `self`, and Instance vs. Class Attributes

These concepts are crucial for understanding how objects are initialized and how data is managed within classes.

### 🔹 The `__init__` Method

- The `__init__` method is a special method (also known as a constructor) that is automatically called when an object is created from a class.
- It is used to initialize the object's attributes.

### Example:

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.is_hungry = True  # Default state
```

## 🔹 self

- self is a reference to the instance of the class.
- It is used to access the attributes and methods of the object within the class.
- By convention, the first parameter of instance methods is named self.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name  # self refers to the current object
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"  # Accessing the object's attribute
```

## Instance vs. Class Attributes

- __Instance Attributes__: Attributes that are specific to each object. They are defined inside the __init__ method using self.
- __Class Attributes__: Attributes that are shared among all objects of the class. They are defined outside the __init__ method and are associated with the class itself.

__Example:__

```python
class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, breed):
        self.name = name  # Instance attribute
        self.breed = breed  # Instance attribute

    def show_species(self):
        return Dog.species  # Accessing the class attribute
```
