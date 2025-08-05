from connector import conn, cursor

# Таблиця студентів
cursor.execute('''
    DELETE
    FROM students;
''')

# Таблиця груп
cursor.execute('''
    DELETE
    FROM groups;
''')

# Таблиця викладачів
cursor.execute('''
    DELETE
    FROM teachers;
''')

# Таблиця предметів
cursor.execute('''
    DELETE
    FROM subjects;
''')

# Таблиця оцінок
cursor.execute('''
    DELETE
    FROM grades;
''')

conn.commit()
conn.close()