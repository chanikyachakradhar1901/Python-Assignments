#Task 1: Encapsulation (User Class)
class User:
    def __init__(self):
        self.__user_name = None
        self.__pwd = None

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name  # password hidden

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")


# Testing
u1 = User()
u1.set_user("john", "1234")
u1.register()
u1.login()

#Task 2: Inheritance (User → Student, Faculty, TempFaculty)

class User:
    def register(self):
        print("User Registered")

    def login(self):
        print("User Logged In")


class Student(User):
    def student_greet(self):
        print("Hello Student")


class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


# Testing
s = Student()
f = Faculty()
t = TempFaculty()

# Child accessing parent methods
s.register()
s.login()
s.student_greet()

f.register()
f.faculty_greet()

t.register()
t.faculty_greet()
t.tempFaculty_greet()

#Task 3: Method Overriding

class User:
    def greet(self):
        print("Welcome User")


class Student(User):
    def greet(self):
        print("Welcome Student")


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")


# Testing
student = Student()
faculty = Faculty()

student.greet()
faculty.greet()

#Task 4: Method Chaining

class User:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self


# Testing
user = User()
user.login().greet().register()


#Task 5: Combined Real-Time System

class User:
    users_count = 0  # class variable

    def __init__(self, username, pwd):
        self.__username = username
        self.__pwd = pwd
        User.users_count += 1

    def get_username(self):
        return self.__username

    def register(self):
        print(f"{self.__username} registered")
        return self

    def login(self):
        print(f"{self.__username} logged in")
        return self

    def greet(self):
        print("Welcome User")
        return self


class Student(User):
    def greet(self):
        print("Welcome Student")
        return self


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self


# Testing
u1 = Student("john", "123")
u2 = Faculty("smith", "456")

u1.login().greet().register()
u2.login().greet().register()

print("Total Users:", User.users_count)