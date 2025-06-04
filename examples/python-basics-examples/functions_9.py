# 🧠 Python Function Basics
# This script demonstrates how to define and use functions in Python.

# ----------------------------------------
# 🛠️ Defining Simple Functions
# ----------------------------------------

# 1️⃣ Function with no parameters
def say_hello():
    print("Hello!")
    print("World")
    print("From")
    print("Function")

# say_hello()  # Output: Hello!



# 2️⃣ Function with parameters
def greet(name):
    print(f"Hi, {name}!")

# greet("Alice")  # Output: Hi, Alice!


# 3️⃣ Function with return value
def square(n):
    return n * n

# result = square(5)
# print(result)  # Output: 25

# ----------------------------------------
# ⚙️ Default and Keyword Arguments
# ----------------------------------------

# 4️⃣ Default arguments
def greet_user(name="Guest"):
    print(f"Welcome, {name}!")

# greet_user()         # Output: Welcome, Guest!
# greet_user("Bob")    # Output: Welcome, Bob!

# 5️⃣ Keyword arguments
def print_info(name, age):
    print(f"{name} is {age} years old.")

# print_info(age=30, name="Eva")  # Named arguments (order doesn't matter)

# ----------------------------------------
# ✨ Return Multiple Values
# ----------------------------------------

# 6️⃣ Returning a tuple
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([4, 1, 9, 2])
# print(low, high)  # Output: 1 9

# ----------------------------------------
# 🔁 Functions with Loops and Conditionals
# ----------------------------------------

# 7️⃣ Factorial using loop
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# print(factorial(5))  # Output: 120

# 8️⃣ Even or odd checker
def is_even(n):
    if n % 2 == 0:
        return True
    return False

# print(is_even(10))  # Output: True
# print(is_even(7))   # Output: False

# ----------------------------------------
# 🧲 Lambda (Anonymous) Functions
# ----------------------------------------

# 9️⃣ Lambda for quick functions
double = lambda x: x * 2
# print(double(4))  # Output: 8

# 🔟 Lambda with sorting
names = ["Bob", "Alice", "Eve"]
sorted_names = sorted(names, key=lambda x: len(x))
# print(sorted_names)  # Output: ['Bob', 'Eve', 'Alice']

# ----------------------------------------
# 🧪 Type Annotations (Optional)
# ----------------------------------------

def add(x: int, y: int) -> int:
    return x + y

# print(add(3, 4))  # Output: 7
