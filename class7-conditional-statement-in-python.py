time: int

time = int(input("Enter a time of day: "))

if 6 <= time < 12:
    print("Good Morning!")
elif 12 <= time < 18:
    print("Good Afternoon!")
else:
    print("Good Night")

