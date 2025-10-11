# DAY 11

## OOP in Code - Encapsulation and Methods (Instance methods, using `self`)

Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP). It involves bundling the data (attributes) and methods that operate on that data within a single unit (a class), and restricting access to some of the object's components.

### 🔹 Encapsulation

- Encapsulation is the concept of bundling data and methods that operate on that data within a class.
- It helps in hiding the internal state of an object and preventing direct access to it from outside the class.
- This is achieved through access modifiers like public, protected, and private.

### Example

```python
class Student:
    def __init__(self, name, rollNo, age):
        self.name = name
        self._rollNo = rollNo  # protected
        self.__age = age  # private

    def __display(self):
        print(f"Hi myself {self.name} {self.__age} year old with roll no : {self._rollNo} from student class")

    def displayPrivateData(self):
        self.__display()


class Branch(Student):  # age can't be accessed here too
    pass


s1 = Student("Rahul", 54, 22)
b1 = Branch("Anurag", 16, 21)
print(b1._rollNo)  # accessible

# print(s1.__age) # not accessible
print(s1._Student__age)
print(dir(s1))
```

### 🔹 Access Modifiers

- **Public**: Accessible from anywhere.
- **Protected**: Accessible within the class and its subclasses (denoted by a single underscore _).
- **Private**: Accessible only within the class (denoted by a double underscore __).

Example:

```python
class Student:
    def __init__(self, name, rollNo, age):
        self.name = name  # public
        self._rollNo = rollNo  # protected
        self.__age = age  # private
```

### 🔹 Getter and Setter Methods

- Getter methods are used to retrieve the values of attributes.
- Setter methods are used to modify the values of attributes.
- They provide a way to control access to the object's attributes and can include validation logic.

### Example

```python
class Student:
    def __init__(self, name, rollNo, age):
        self.name = name
        self._rollNo = rollNo
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        # we can also add some logic like age limit for update
        self.__age = age

    def __display(self):
        print(f"Hi myself {self.name} {self.__age} year old with roll no : {self._rollNo} from student class")

    def displayPrivateData(self):
        self.__display()


s1 = Student("Anurag", 23, 20)
print(s1._Student__age)
s1._Student__display()

print(s1.get_age())
s1.set_age(22)
print(s1.get_age())```
