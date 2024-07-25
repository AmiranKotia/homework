# # Davaleba 12
# collection = {}

# def add_book(author, title, genre):
#     if author not in collection:
#         collection[author] = []
#     collection[author].append({'title': title, 'genre': genre})
#     print("წიგნი დაემატა კოლექციას.")

# def search_author(author_name):
#     return collection.get(author_name, [])

# def all_books():
#     return collection

# def main():
#     while True:
#         action = input("შეიყვანეთ რომელიმე: (add/title/author/end): ").strip().lower()
#         if action == "end":
#             break
#         elif action == "add":
#             title = input("შეიყვანეთ წიგნის სახელწოდება: ").strip()
#             author = input("შეიყვანეთ ავტორის სახელი: ").strip()
#             genre = input("შეიყვანეთ ჟანრი: ").strip()
#             add_book(author, title, genre)
#         elif action == "author":
#             author_name = ("შეიყვანეთ ავტორის სახელი: ").strip()
#             books = search_author(author_name)
#             if books:
#                 print(f"წიგნები {author_name} მიერ:")
#                 for book in books:
#                     print(f"სახელწოდება: {book['title']}, ჟანრი: {book['genre']}")
#             else:
#                 print(f"{author_name} ავტორის სახელით წიგნი არ მოიძებნა.")
#         elif action == "title":
#             title_name = input("შეიყვანეთ წიგნის სახელწოდება: ").strip()
#             found = False
#             for author, books in collection.items():
#                 for book in books:
#                     if book['title'].lower() == title_name.lower():
#                         print(f"მოიძებნა: \"{book['title']}\" {author}-ს მიერ, ჟანრი: {book['genre']}")
#                         found = True
#                 if not found:
#                     print(f"წიგნი დასახელებით {title_name} არ მოიძებნა.")
#         elif action == "all":
#             print(all_books())
#         else:
#             print("არასწორი ბრძანება. გთხოვთ შეიყვანოთ რომელიმე: (add/title/author/end): ")

# main()



# # Davaleba 13:
# lst = ["red", "Green", "white", "Black", "Pink", "yellow"]

# file_name = "output.txt"

# with open(file_name, "w") as file:
#     for item in lst:
#         file.write(item + "\n")

# print("List contents have been saved to", file_name)


# def count_uppercase(file_name):
#     uppercase_count = 0

#     with open(file_name, "r") as file:
#         for line in file:
#             line = line.strip()
#             for item in line:
#                 if item.isupper():
#                     uppercase_count += 1
#     return uppercase_count            
    
# file_name = "output.txt"
# uppercase_count = count_uppercase(file_name)
# print("მაღალ რეგისტრში დაწერილი სიტყვების რაოდენობა: ", uppercase_count)



# # Davaleba 14:
# import csv

# def calculate_average_scores(file_name):
#     scores = {}

#     with open(file_name, "r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             full_name = row["FullName"]
#             score = int(row["Score"])
#             if full_name not in scores:
#                 scores[full_name] = []
#             scores[full_name].append(score)

#     averages = {full_name: sum(scores)/len(scores) for full_name, scores in scores.items()}

#     return scores, averages

# file_name = 'student_scores.csv'
# scores, averages = calculate_average_scores(file_name)

# print(f"Student's scores: {scores}")
# print(f"Average scores: {averages}")



# # Davaleba 16:
# class ShoppingCart:
#     def __init__(self):
#         self.items = {}
#         self.prices = {
#             "პური": 1.50,
#             "კარაქი": 2.00,
#             "წყალი": 0.75,
#             "ზეთი": 3.50
#         }
    
#     def add_item(self, item_name, quantity):
#         if item_name in self.items:
#             self.items[item_name] += quantity
#         else:
#             self.items[item_name] = quantity

#     def remove_item(self, item_name):
#         if item_name in self.items:
#             del self.items[item_name]

#     def current_items(self):
#         return self.items
    
#     def calculate_total(self):
#         total = 0
#         for item_name, quantity in self.items.items():
#             if item_name in self.prices:
#                 total += self.prices[item_name] * quantity
#         return total

# cart = ShoppingCart()
# cart.add_item("პური", 2)
# cart.add_item("კარაქი", 1)
# cart.add_item("წყალი", 6)
# cart.add_item("ზეთი", 2)

# print("ამჟამად კალათაშია:")
# print(cart.current_items())
# print(f"ჯამი: {cart.calculate_total()}")

# cart.remove_item("ზეთი")

# print("ამჟამად კალათაშია:")
# print(cart.current_items())
# print(f"ჯამი: {cart.calculate_total()}")



# # Davaleba 17:
# class User:
#     def __init__(self, username):
#         self.username = username
#         self.posts = []
#         self.friends = set()

#     def create_post(self, content):
#         post = Post(content, self)
#         self.posts.append(post)
#         return post

#     def like_post(self, post):
#         post.add_like()

# class Post:
#     def __init__(self, content, author):
#         self.content = content
#         self.author = author
#         self.comments = []
#         self.likes = 0

#     def add_comment(self, comment):
#         self.comments.append(comment)

#     def add_like(self):
#         self.likes += 1

# class Comment:
#     def __init__(self, content, author):
#         self.content = content
#         self.author = author

# user1 = User("User1")
# user2 = User("User2")
# user1.friends.add(user2)

# user1.create_post("Today is a great day for studying.")
# post2 = user1.create_post("Went for a nice walk with my dog.")
# post2.add_comment(Comment("I am happy for you", post2))
# user1.like_post(post2)
# user2.like_post(post2)



# # Davaleba 18:
# class Person:
#     def __init__(self, name, deposit=1000, loan=0):
#         self.name = name
#         self.deposit = deposit
#         self.loan = loan
    
#     def __str__(self):
#         return f"Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"
    
# class House:
#     def __init__(self, ID, price, owner=None, status="გასაყიდი"):
#         self.ID = ID
#         self.price = price
#         self.owner = owner
#         self.status = status

#     def sell(self, buyer, loan_amount=0):
#         if loan_amount > 0:
#             buyer.deposit += loan_amount
#             self.owner = buyer
#             self.status = "გაყიდული სესხით"
#             self.owner.loan += loan_amount
#             print(f"The house with ID {self.ID} has been sold with a loan of {loan_amount}.")
#         else:
#             self.owner.deposit += self.price
#             buyer.deposit -= self.price
#             self.owner = buyer
#             self.status = "გაყიდული"
#             print(f"The house with ID {self.ID} has been sold.")

# person1 = Person("Davit Apakidze")
# person2 = Person("Lasha Papava")
# house = House(123, 200000, owner=person1)

# house.price = 220000
# house.sell(person2, loan_amount = 50000)
# print(person1)
# print(person2)



# # Davaleba 19:
# class Roman:
#     def __init__(self):
#         self.roman_numerals = {
#             'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9,
#             'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
#         }
    
#     def convert_to_decimal(self, roman):
#         decimal = 0
#         previous_value = 0
#         for i in roman[::-1]:
#             value = self.roman_numerals[i]
#             if value < previous_value:
#                 decimal -= value
#             else:
#                 decimal += value

#             previous_value = value
#         return decimal

# result = Roman().convert_to_decimal("MMDVCML")
# print(result)



# # Davaleba 20:
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def printLeafNodes(root):
#     if root is None:
#         return
#     if root.left is None and root.right is None:
#         print(root.value)
#     else:
#         printLeafNodes(root.left)
#         printLeafNodes(root.right)

# def main():
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.left.left = TreeNode(4)
#     root.left.right = TreeNode(5)
#     root.right.left = TreeNode(6)
#     root.right.right = TreeNode(7)

#     print("Leaf nodes of the binary tree:")
#     printLeafNodes(root)

# if __name__ == "__main__":
#     main()



# # Davaleba 21:
# import json

# class Student:
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades

#     @classmethod
#     def read_json(cls, filename):
#         with open(filename, 'r') as file:
#             data = json.load(file)
#             students_data = data["students"]
#             students = []
#             for i in students_data:
#                 student = cls(i["name"], i["age"], i["grades"])
#                 students.append(student)
#             return students

#     @staticmethod    
#     def calculate_average_grade(student):
#         return sum(student.grades) / len(student.grades)
    
#     @staticmethod
#     def write_json(students, filename):
#         average_grades = {student.name: Student.calculate_average_grade(student) for student in students}
#         with open(filename, "w") as file:
#             json.dump(average_grades, file, indent=4)

# def main():
#     students = Student.read_json("C:\\Users\\akoti\\OneDrive - Girteka Competence Center, UAB\\Desktop\\AK.PRG\\Homework\\Homework\\students.json")
#     for student in students:
#         average_grade = Student.calculate_average_grade(student)
#         print(f"{student.name}: {average_grade}")

#     Student.write_json(students, "average_grades.json")

# if __name__ == "__main__":
#     main()



# # Davaleba 22:
# import json
# from faker import Faker
# import random

# fake = Faker()

# class Student:
#     def __init__(self, student_id, name, email, age, active):
#         self.student_id = student_id
#         self.name = name
#         self.email = email
#         self.age = age
#         self.active = active

#     def to_dict(self):
#         return {
#             "student_id": self.student_id,
#             "name": self.name,
#             "email": self.email,
#             "age": self.age,
#             "active": self.active
#         }

# class StudentGenerator:
#     def __init__(self, num_students):
#         self.num_students = num_students

#     def generate_students(self):
#         students = []
#         for _ in range(self.num_students):
#             student_id = fake.uuid4()
#             name = fake.name()
#             email = fake.email()
#             age = random.randint(18, 25)
#             active = random.choice([True, False])
#             student = Student(student_id, name, email, age, active)
#             students.append(student)
#         return students

#     def sort_students(self, students):
#         active_students = [student.to_dict() for student in students if student.active]
#         inactive_students = [student.to_dict() for student in students if not student.active]
#         return active_students, inactive_students

# num_students = 100
# generator = StudentGenerator(num_students)
# students = generator.generate_students()
# active_students, inactive_students = generator.sort_students(students)

# sorted_students = active_students + inactive_students

# sorted_students_json = json.dumps(sorted_students, indent=4)

# # print(sorted_students_json)

# with open('students.json', 'w') as file:
#     file.write(sorted_students_json)

# with open('students.json', 'r') as file:
#     students_data = file.read()

# students = json.loads(students_data)
# for student in students:
#     print(student)



# # Davaleba 26:
# import pytest

# def reverse_string(s):
#     return s[::-1]

# def is_palindrome(s):
#     return s == s[::-1]

# def capitalize_words(s):
#     return " ".join(word.capitalize() for word in s.split())

# def celsius_to_fahrenheit(c):
#     return c * 9/5 +32

# def fahrenheit_to_celsius(f):
#     return (f - 32) * 5/9

# def test_reverse_string():
#     assert reverse_string("hello") == "olleh"
#     assert reverse_string("world") == "dlrow"

# def test_os_palindrome():
#     assert is_palindrome("madam") is True
#     assert is_palindrome("hello") is False

# def test_capitalize_words():
#     assert capitalize_words("hello world") == "Hello World"
#     assert capitalize_words("python programming") == "Python Programming"

# def test_celsius_to_fahrenheit():
#     assert celsius_to_fahrenheit(0) == pytest.approx(32)
#     assert celsius_to_fahrenheit(100) == pytest.approx(212)

# def test_fahrenheit_to_celsius():
#     assert fahrenheit_to_celsius(32) == pytest.approx(0)
#     assert fahrenheit_to_celsius(212) == pytest.approx(100)

# if __name__ == "__main__":
#     pytest.main()



# # Davaleba 27:
# import json
# import threading

# def parse_and_print_json(filename):
#     try:
#         with open(filename, "r") as file:
#             data = json.load(file)
#             print(f"Data from {filename}: {data}")
#     except Exception as e:
#         print(f"Error reading {filename}: {e}")

# def main():
#     filenames = ["student1.json", "student2.json", "student3.json"]
#     threads = []

#     for filename in filenames:
#         thread = threading.Thread(target=parse_and_print_json, args=(filename,))
#         threads.append(thread)
#         thread.start()

#     for thread in threads:
#         thread.join()

# if __name__ == "__main__":
#     main()




# # Davaleba 32:
# import sqlite3

# conn = sqlite3.connect('main.db')
# cursor = conn.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Authors (
#             author_id INTEGER PRIMARY KEY,
#             name TEXT NOT NULL
#     )
# ''')

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Books (
#         book_id INTEGER PRIMARY KEY,
#         title TEXT NOT NULL,
#         author_id INTEGER,
#         FOREIGN KEY (author_id) REFERENCES Authors (author_id)
#     )
# ''')

# conn.commit()


# authors = [(1, 'J.K Rowling'), (2, 'J.K. Tolkien')]
# cursor.executemany('''
#     INSERT INTO Authors (author_id, name)
#     VALUES (?, ?)
# ''', authors)

# conn.commit()


# books = [(1, 'Harry Potter and the Sorcerer\'s Stone', 1), (2, 'The Hobbit', 2)]
# cursor.executemany('''
#     INSERT INTO Books (book_id, title, author_id)
#     VALUES (?, ?, ?)
# ''', books)

# conn.commit()


# cursor.execute('SELECT * FROM Authors')
# authors = cursor.fetchall()
# print('Authors:')
# for author in authors:
#     print(author)

# cursor.execute('SELECT * FROM Books')
# book = cursor.fetchall()
# print('\nBooks:')
# for book in books:
#     print(book)

# conn.close()




# # Davaleba 33:
# from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
# from sqlalchemy.orm import declarative_base, sessionmaker, relationship
# from datetime import date
# import os

# if os.path.exists('example.db'):
#     os.remove('example.db')

# engine = create_engine('sqlite:///example.db')
# Base = declarative_base()

# class Department(Base):
#     __tablename__ = 'departments'
#     DepartmentID = Column(Integer, primary_key=True, autoincrement=True)
#     DepartmentName = Column(String, nullable=False)

# class Employee(Base):
#     __tablename__ = 'employees'
#     EmployeeID = Column(Integer, primary_key=True, autoincrement=True)
#     Fullname = Column(String, nullable=False)
#     HireDate = Column(Date, nullable=False)
#     DepartmentID = Column(Integer, ForeignKey('departments.DepartmentID'), nullable=False)
#     department = relationship('Department')

# Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# departments = [
#     Department(DepartmentName='HR'),
#     Department(DepartmentName='IT'),
#     Department(DepartmentName='Finance')
# ]
# session.add_all(departments)
# session.commit()

# employees = [
#     Employee(Fullname='Giorgi Gelashvili', HireDate=date(2021, 1, 10), DepartmentID=1),
#     Employee(Fullname='Kote Lashkhia', HireDate=date(2020, 5, 22), DepartmentID=2),
#     Employee(Fullname='Vladimer Shavadze', HireDate=date(2019, 8, 14), DepartmentID=3)
# ]
# session.add_all(employees)
# session.commit()

# all_departments = session.query(Department).all()
# print("Departments:")
# for dept in all_departments:
#     print(f"ID: {dept.DepartmentID}, Name: {dept.DepartmentName}")

# all_employees = session.query(Employee).all()
# print("\nEmployees:")
# for emp in all_employees:
#     print(f"ID: {emp.EmployeeID}, Name: {emp.Fullname}, Hire Date: {emp.HireDate}, Department ID: {emp.DepartmentID}")

# session.close()
