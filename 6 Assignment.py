
# Task 1: User Info Manager


users = []

def create_user(name, age, role):
    user = {
        "name": name.title(),   # formatting with .title()
        "age": age,
        "role": role.title()
    }
    return user

# Adding multiple users
users.append(create_user("chanikya", 22, "developer"))
users.append(create_user("sai", 25, "tester"))
users.append(create_user("ravi", 23, "analyst"))

# Print all users
print("---- User List ----")
for user in users:
    print(user)

# Task 2: Dynamic Calculator (*args)


def calculate_total(*numbers):
    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0
    return total, avg

result = calculate_total(10, 20, 30, 40)
print("\n---- Calculator ----")
print("Total:", result[0])
print("Average:", result[1])



# Task 3: Keyword Config (**kwargs)


def system_config(**settings):
    print("\n---- System Config ----")
    for key, value in settings.items():
        print(f"{key}: {value}")

# Example
system_config(mode="debug", version="1.0", user="admin")

system_config(mode="debug", version="1.0")



# Task 4: Factorial (Recursion)

def factorial(n):
    if n < 0:
        return "Error: Negative numbers not allowed"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test
print("\n---- Factorial ----")
print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
print("Factorial of -3:", factorial(-3))


# Task 5: Generator vs List


def square_generator(n):
    for i in range(n):
        yield i * i

# Normal list
square_list = [i*i for i in range(5)]

# Generator
square_gen = square_generator(5)

print("\n---- Memory Comparison ----")
print("List:", square_list)
print("Generator:", list(square_gen))

# Type comparison
print("Type of list:", type(square_list))
print("Type of generator:", type(square_generator(5)))


# Task 6: Exception Handling


print("\n---- Exception Handling ----")

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    
    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")

finally:
    print("Program Completed")


# Task 7: File Handling


print("\n---- File Handling ----")

# Writing to file (BEST PRACTICE)
with open("team_data.txt", "w") as file:
    for user in users:
        file.write(f"{user['name']}, {user['age']}, {user['role']}\n")

# Check if file is closed after writing
print("File closed after writing:", file.closed)


# Reading file (BEST PRACTICE)
with open("team_data.txt", "r") as file:
    content = file.read()
    print("\nFile Content:\n", content)

# Check if file is closed after reading
print("File closed after reading:", file.closed)