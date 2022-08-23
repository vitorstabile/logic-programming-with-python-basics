<h1 align="center"> Python </h1>

# Content

1. [Chapter 1: The Python Language](#chapter1)
    - [Chapter 1 - Part 1: First Program in Python](#chapter1part1)
    - [Chapter 1 - Part 2: Variables Types in Python](#chapter1part2)
    - [Chapter 1 - Part 3: Data Output in Python](#chapter1part3)
    - [Chapter 1 - Part 4: Data Processing in Python](#chapter1part4)
    - [Chapter 1 - Part 5: Data Casting in Python](#chapter1part5)
    - [Chapter 1 - Part 6: Data Input in Python](#chapter1part6)
    - [Chapter 1 - Part 7: Conditional Statement in Python](#chapter1part7)
    - [Chapter 1 - Part 8: While Statement in Python](#chapter1part8)
    - [Chapter 1 - Part 9: For Statement in Python](#chapter1part9)
    - [Chapter 1 - Part 10: Vectors in Python](#chapter1part10)
    - [Chapter 1 - Part 11: Matrix in Python](#chapter1part11)
2. [Chapter 2: Object Oriented](#chapter2)
    - [Chapter 2 - Part 1: Abstraction](#chapter2part1)
    - [Chapter 2 - Part 2: Encapsulation](#chapter2part2)
    - [Chapter 2 - Part 3: Inheritance](#chapter2part3)
    - [Chapter 2 - Part 4: Polymorphism](#chapter2part4)
    
## <a name="chapter1"></a>Chapter 1: The Python Language

#### <a name="chapter1part1"></a>Chapter 1 - Part 1: First Program in Python

```python

print("Hello World!")

```

#### <a name="chapter1part2"></a>Chapter 1 - Part 2: Variables Types in Python

```python

age: int
salary: float
height: float
genre: str
name: str

age = 20
salary = 5800.5
height = 1.63
genre = "F"
name = "Maria Silva"

print(f"AGE = {age}")
print(f"SALARY = {salary:.2f}")
print(f"HEIGHT = {height:.2f}")
print(f"GENRE = {genre}")
print(f"NAME = {name}")

```

#### <a name="chapter1part3"></a>Chapter 1 - Part 3: Data Output in Python

```python

print("Good Morning", end="")
print("Good Night", end="")

print()

print("Good Morning")
print("Good Night")

x: int; y: int
x = 10
y = 20
print(x)
print(y)

z: float
z = 2.3456
print("{:.2f}".format(z))

age: int
salary: float
name: str
genre: str

age = 32
salary = 4560.9
name = "Maria Silva"
genre = "F"

print(f"The employee {name}, genre {genre}, earn {salary:.2f} and have {age} years old")

print("The employee {:s}, genre {:s}, earn {:.2f} and have {:d} years old".format(name, genre, salary, age))

```

#### <a name="chapter1part4"></a>Chapter 1 - Part 4: Data Processing in Python

```python

x1: int
y1: int
x1 = 5
y1 = 2 * x1
print(x1)
print(y1)

x2: int
y2: float
x2 = 5
y2 = 2 * x2
print(x2)
print(f"{y2:.1f}")

b1: float
b2: float
h: float
area: float
b1 = 6.0
b2 = 8.0
h = 5.0
area = (b1 + b2) / 2.0 * h
print(area)

a: int
b: int
result: int
a = 5
b = 2
result = a // b
print(result)

```

#### <a name="chapter1part5"></a>Chapter 1 - Part 5: Data Casting in Python

```python

a: float
b: int
a = 5.0
b = int(a)
print(b)

```

#### <a name="chapter1part6"></a>Chapter 1 - Part 6: Data Input in Python

```python

salary1: float
salary2: float
name1: str
name2: str
age: int
genre: str

name1 = input("Name of the first person: ")
salary1 = float(input("Salary of the first person: "))

name2 = input("Name of the second person: ")
salary2 = float(input("Salary of the second person: "))

age = int(input("Age: "))
genre = input("Genre (F/M): ")

print(f"Name 1: {name1}")
print(f"Salary 1: {salary1:.2f}")
print(f"Name 2: {name2}")
print(f"Salary 2: {salary2:.2f}")
print(f"Age: {age}")
print(f"Genre: {genre}")

```

#### <a name="chapter1part7"></a>Chapter 1 - Part 7: Conditional Statement in Python

```python

time: int

time = int(input("Enter a time of day: "))

if 6 <= time < 12:
    print("Good Morning!")
elif 12 <= time < 18:
    print("Good Afternoon!")
else:
    print("Good Night")

```

#### <a name="chapter1part8"></a>Chapter 1 - Part 8: While Statement in Python

```python

x: int
sum: int

sum = 0
x = int(input("Enter the first number: "))

while x != 0:
    sum = sum + x
    x = int(input("Enter another number: "))

print("SUM = ", sum)

```

#### <a name="chapter1part9"></a>Chapter 1 - Part 9: For Statement in Python

```python

x: int
sum: int

N = int(input("How many number will be enter? "))

sum = 0
for i in range(0, N):
    x = int(input("Enter a number: "))
    sum = sum + x

print("SUM = ", sum)

```

#### <a name="chapter1part10"></a>Chapter 1 - Part 10: Vectors in Python

```python

N: int
N = int(input("How many numbers will be enter? "))
vet: [float] = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input("Enter a number: "))

print()
print("TYPED NUMBERS")
for i in range(0, N):
    print(f"{vet[i]:.1f}")

```

#### <a name="chapter1part11"></a>Chapter 1 - Part 11: Matrix in Python

```python

M: int
N: int

M = int(input("How many rows the matrix will be? "))
N = int(input("How many columns the matrix will be? "))

mat: [[int]] = [[0 for x in range(N)] for x in range(M)]

for i in range(0, M):
    for j in range(0, N):
        mat[i][j] = int(input(f"Element [{i},{j}]: "))

print()
print("Typed Matrix:")
for i in range(0, M):
    for j in range(0, N):
        print(f"{mat[i][j]} ", end="")
    print()

```
## <a name="chapter2"></a>Chapter 2: Object Oriented

#### <a name="chapter2part1"></a>Chapter 2 - Part 1: Abstraction

How it represents a real object in our system. It must have identity (Class) given by properties (attributes) and methods (functions).

o Class: Structured type that can contain members - Representation of an entity (Product, Customer), service (ProductService, CustomerService), drivers (ProductController), utilities (calculator) and others (views, repositories).
o Attributes (Data or Fields - Ex: Customer has attribute name, email, cpf and etc.)
o Methods (Class functions and operations - Ex: Consult email, consult cpf, change cpf)

• A class can also have:
o Constructors (Special class operation, performed at instantiation of the class. Used to start attribute values ​​or to force the object to receive data or dependency on its instantiation (Dependency injection))
o Overload of constructors or methods (Esoecify more than one constructor or method in the class)
Encapsulation (Getters and Setters)
o Inheritance (from whom this class inherits)
Polymorphism (A class has several forms or functions)

• Object: They are the instance of the class or instance of the type - Ex: Product p1, Client customer1
• Class: It is the definition of the type (Customer Class, Product Class)

• Instantiation: When we instantiate primitive variables (double, int, String ...) it is instantiated in the memory stack. When the command New in Objects, Arrays and Lists is communicated, the dynamic location of memory occurs, where the object is allocated in another area of memory, called Heap and the object will point to the memory address.

• Advantages of object orientation:
o Reuse of the code and delegation of responsibilities

#### <a name="chapter2part2"></a>Chapter 2 - Part 2: Encapsulation

Adds security to an object-oriented application, as it hides class properties.

o An object must not expose any attributes (use of access modifiers - private, protected ...)
o Class attributes are usually accessed by special methods (Getters and Setters), avoiding direct access to the object's property.
o Analogy with a television: When you click on the call button, we do not know what happens internally on the TV. We can say that the methods that connect the TV are encapsulated.

#### <a name="chapter2part3"></a>Chapter 2 - Part 3: Inheritance

Type of association between classes that allows a class to inherit all data and behavior from another

o Can be used for code reuse
o Used for polymorphism - A class has several uses
The whole class java me, inherits from Object (Warper Classes)

#### <a name="chapter2part4"></a>Chapter 2 - Part 4: Polymorphism

A feature that allows variables of the same more generic type to be able to point to objects of different specific types, thus having different behaviors according to each specific type. In some cases, we must perform the upcasting or dowcasting of the object.

<!-- URL's -->
