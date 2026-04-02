from abc import ABC, abstractmethod
from functools import reduce

# ==============================
# Task 2: Abstraction
# ==============================
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


# ==============================
# Task 1: super() + Class Design
# ==============================
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"User: {self.name}, ID: {self.id}"


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)   
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)   
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, ID: {self.id}, Salary: {self.salary}"


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)   
        self.duration = duration

    def get_details(self):
        return f"TempFaculty: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"


# ==============================
# Data Creation (Final Challenge)
# ==============================
students = [
    Student("John", 1, "CSE", 60000),
    Student("Alice", 2, "ECE", 45000),
    Student("Bob", 3, "IT", 70000),
    Student("David", 4, "CSE", 30000)
]

faculty = [
    Faculty("Dr.Smith", 101, 40000),
    Faculty("Dr.Jane", 102, 25000),
    TempFaculty("Mr.Raj", 103, 35000, "6 months"),
    TempFaculty("Ms.Anita", 104, 28000, "3 months")
]


# ==============================
# Task 7: Higher Order Function
# ==============================
def process_users(users, func):
    return list(map(func, users))


# ==============================
# FINAL EXECUTION
# ==============================

# 1. All Details (Abstraction)
print("\n--- ALL USER DETAILS ---")
for user in students + faculty:
    print(user.get_details())


# ==============================
# Task 3: Sorting
# ==============================
print("\n--- STUDENTS SORTED BY FEES ---")
sorted_students = sorted(students, key=lambda x: x.fees)
for s in sorted_students:
    print(s.get_details())

print("\n--- FACULTY SORTED BY SALARY ---")
sorted_faculty = sorted(faculty, key=lambda x: x.salary)
for f in sorted_faculty:
    print(f.get_details())


# ==============================
# Task 4: map()
# ==============================
print("\n--- STUDENT NAMES (map) ---")
student_names = list(map(lambda s: s.name, students))
print(student_names)


# ==============================
# Task 5: filter()
# ==============================
print("\n--- HIGH FEE STUDENTS (>50000) ---")
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
for s in high_fee_students:
    print(s.get_details())

print("\n--- HIGH SALARY FACULTY (>30000) ---")
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))
for f in high_salary_faculty:
    print(f.get_details())


# ==============================
# Task 6: reduce()
# ==============================
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("\n--- TOTALS ---")
print("Total Fees Collected:", total_fees)
print("Total Salary Paid:", total_salary)


# ==============================
# Task 7 + Final Challenge Combined
# (map + filter + reduce together)
# ==============================
print("\n--- COMBINED FUNCTIONAL PROGRAMMING ---")

total_high_fees = reduce(
    lambda acc, x: acc + x,
    map(lambda s: s.fees,
        filter(lambda s: s.fees > 50000, students)),
    0
)

print("Total Fees (Students >50000):", total_high_fees)


# ==============================
# Higher Order Function Usage
# ==============================
print("\n--- USING HIGHER ORDER FUNCTION ---")
upper_names = process_users(students, lambda s: s.name.upper())
print(upper_names)