from connector import cursor, conn
from faker import Faker
import random


faker = Faker('uk-Ua')

# Заповнення таблиці груп
group_names = ['Group A', 'Group B', 'Group C']
for name in group_names:
    cursor.execute('INSERT INTO groups (name) VALUES (?)', (name,))

# Заповнення таблиці викладачів
teachers = []
for _ in range(5):
    first_name = faker.first_name()
    last_name = faker.last_name()
    cursor.execute('INSERT INTO teachers (first_name, last_name) VALUES (?, ?)', (first_name, last_name))
    teachers.append(cursor.lastrowid)

# Заповнення таблиці предметів
subject_names = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'Literature', 'Art']
for name in subject_names:
    teacher_id = random.choice(teachers)
    cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (name, teacher_id))

# Заповнення таблиці студентів
students = []
group_ids = [1, 2, 3]
for _ in range(50):
    first_name = faker.first_name()
    last_name = faker.last_name()
    group_id = random.choice(group_ids)
    cursor.execute('INSERT INTO students (first_name, last_name, group_id) VALUES (?, ?, ?)',
                   (first_name, last_name, group_id))
    students.append(cursor.lastrowid)

# Заповнення таблиці оцінок
subject_ids = list(range(1, len(subject_names) + 1))
for student_id in students:
    for _ in range(random.randint(10, 20)):
        subject_id = random.choice(subject_ids)
        grade = random.randint(1, 10)
        date_of_grade = faker.date_this_year()
        cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date_of_grade) VALUES (?, ?, ?, ?)',
                       (student_id, subject_id, grade, date_of_grade))

conn.commit()
conn.close()
