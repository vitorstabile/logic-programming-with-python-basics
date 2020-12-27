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

