from idlelib import query
from sqlite3 import DatabaseError
from connector import conn
import logging

get_subject_ids_query = "SELECT id FROM subjects"

get_teacher_ids_query = "SELECT id FROM teachers"

get_group_ids_query = "SELECT id FROM groups"

get_student_ids_query = "SELECT id FROM students"

def read_query(query_file):
    with open(query_file, 'r') as query:
        return query.read()

def get_entity_ids(cursor, query):
    cursor.execute(query)
    return [row[0] for row in c.fetchall()]

def find_top5_students(cursor, query):
    return cursor.execute(query).fetchall()

def find_best_student_of_subject(cursor, query, subject_id):
    return cursor.execute(query, (subject_id,)).fetchone()

def find_avg_grade_in_groups_of_subject(cursor, query, subject_id):
    return cursor.execute(query, (subject_id,)).fetchone()

def find_avg_grade(cursor, query):
    return cursor.execute(query).fetchone()

def find_subjects_of_teacher(cursor, query, teacher_id):
    return cursor.execute(query, (teacher_id,)).fetchall()

def find_students_by_group(cursor, query, group_id):
    return cursor.execute(query, (group_id,)).fetchall()

def find_grades_of_students_in_group_by_subject(cursor, query, group_id, subject_id):
    return cursor.execute(query, (group_id, subject_id,)).fetchall()

def execute_task_for_each_id(function, function_query, ids_query, cursor):
    ids = get_entity_ids(cursor, ids_query)
    return [function(cursor, function_query, id) for id in ids]


try:
    if conn is not None:
        c = conn.cursor()

        print("1) ", find_top5_students(c, read_query('query_1.sql')), "\n")

        query_2 = read_query('query_2.sql')
        print("2) ", execute_task_for_each_id(find_best_student_of_subject, query_2, get_subject_ids_query, c), "\n")

        query_3 = read_query('query_3.sql')
        print("3) ", execute_task_for_each_id(find_avg_grade_in_groups_of_subject, query_3, get_subject_ids_query, c), "\n")

        print("4) ", find_avg_grade(c, read_query('query_4.sql')), "\n")

        query_5 = read_query('query_5.sql')
        print("5) ", execute_task_for_each_id(find_subjects_of_teacher, query_5, get_teacher_ids_query, c), "\n")

        query_6 = read_query('query_6.sql')
        print("6) ", execute_task_for_each_id(find_students_by_group, query_6, get_group_ids_query, c), "\n")



except DatabaseError as err:
    logging.error(err)
except RuntimeError as err:
    logging.error(err)
except Exception as err:
    logging.error(err)
# try:
#     if conn is not None:
#         c = conn.cursor()
#         try:




#             for group in groups:
#                 group_id = group[0]
#                 for subject in subjects:
#                     subject_id = subject[0]
#                     c.execute(query_7, (group_id,subject_id,))
#                     print(c.fetchall())

#             for teacher in teachers:
#                 teacher_id = teacher[0]
#                 c.execute(query_8, (teacher_id,))
#                 print(c.fetchall())

#             c.execute(select_students)
#             students = c.fetchall()
#             for student in students:
#                 student_id= student[0]
#                 c.execute(query_9, (student_id,))
#                 print(c.fetchall())

#             for student in students:
#                 student_id = student[0]
#                 for teacher in teachers:
#                     teacher_id = teacher[0]
#                     c.execute(query_10, (student_id,teacher_id,))
#                     print(c.fetchall())

#         except DatabaseError as e:
#             logging.error(e)
#         finally:
#             conn.close()
#     else:
#         print("Error! cannot create the database connection.")
# except RuntimeError as err:
#     logging.error(err)
