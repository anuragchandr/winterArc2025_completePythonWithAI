# DAY15

## 📘 1. Inheritance

**Definition:**  
Inheritance allows a class (child/subclass) to acquire properties and methods from another class (parent/superclass).

### 🔹 Example

```python
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return "Woof!"


dog = Dog()

print(dog.speak())   # Output: Woof!
```

## ⚙️ 2. Multiple Inheritance

__Definition:__
A class can inherit from more than one parent class.

#### ___🔹 Example___

```python
class Father:
    def skill(self):
        return "Business"

class Mother:
    def hobby(self):
        return "Cooking"

class Child(Father, Mother):  # inherits from both
    def talent(self):
        return "Singing"

c = Child()
print(c.skill())   # From Father
print(c.hobby())   # From Mother
print(c.talent())  # Own method

```

## 🧠 3. super() Function

__Definition:__
super() is used to call methods from the parent class without directly naming it — useful when extending functionality.

#### ___🔹 Example (Single Inheritance)___

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # Call parent __init__
        self.breed = breed

dog = Dog("Tommy", "Labrador")
print(dog.name, dog.breed)

```
#### ___🔹 Example (Multiple Inheritance)___

```python
class A:
    def show(self):
        print("From A")

class B(A):
    def show(self):
        super().show()
        print("From B")

class C(B):
    def show(self):
        super().show()
        print("From C")

obj = C()
obj.show()

```
