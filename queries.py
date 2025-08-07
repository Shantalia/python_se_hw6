from connector import conn, cursor

# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
cursor.execute('''
    SELECT student_id, AVG(grade) as avg_grade
    FROM grades
    GROUP BY student_id
    ORDER BY avg_grade DESC
    LIMIT 5;
''')

# Знайти студента із найвищим середнім балом з певного предмета.
subjects = cursor.fetchall()
for subject in subjects:
    cursor.execute('''
        SELECT student_id, AVG(grade) as avg_grade
        FROM grades
        WHERE subject_id = ?
        GROUP BY student_id
        ORDER BY avg_grade DESC
        LIMIT 1;
    ''', (subject[0],))

# Знайти середній бал у групах з певного предмета.
for subject in subjects:
    cursor.execute('''
        SELECT g.name, AVG(gr.grade) as avg_grade
       FROM grades gr
        JOIN students s ON gr.student_id = s.id
        JOIN groups g ON s.group_id = g.id
        WHERE gr.subject_id = ?
        GROUP BY g.name;
    ''', (subject[0],))

# Знайти середній бал на потоці (по всій таблиці оцінок).
cursor.execute('''
    SELECT AVG(grade) as avg_grade
    FROM grades;
''')

conn.close()