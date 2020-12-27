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

