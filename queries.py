from sqlite3 import DatabaseError
from sqlite3_connector import conn
import logging

example_teacher_id = 5
example_student_id = 18
example_group_id = 2
example_subject_id = 3
example_grade_id = 7

def read_query(query_file):
    with open(query_file, 'r') as query:
        return query.read()


try:
    if conn is not None:
        c = conn.cursor()

        query_1 = read_query('query_1.sql')
        print(f"1) {c.execute(query_1).fetchall()} \n")

        query_2 = read_query('query_2.sql')
        print(f"2) {c.execute(query_2, (example_subject_id, )).fetchone()} \n")

        query_3 = read_query('query_3.sql')
        print(f"3) {c.execute(query_3, (example_subject_id, )).fetchall()} \n")

        query_4 = read_query('query_4.sql')
        print(f"4) {c.execute(query_4).fetchone()} \n")

        query_5 = read_query('query_5.sql')
        print(f"5) {c.execute(query_5, (example_teacher_id, )).fetchall()} \n")

        query_6 = read_query('query_6.sql')
        print(f"6) {c.execute(query_6, (example_group_id, )).fetchall()} \n")

        query_7 = read_query('query_7.sql')
        print(f"7) {c.execute(query_7, (example_group_id, example_subject_id, )).fetchall()} \n")

        query_8 = read_query('query_8.sql')
        print(f"8) {c.execute(query_8, (example_teacher_id, )).fetchone()} \n")

        query_9 = read_query('query_9.sql')
        print(f"9) {c.execute(query_9, (example_student_id,)).fetchall()} \n")

        query_10 = read_query('query_10.sql')
        print(f"10) {c.execute(query_10, (example_student_id, example_teacher_id, )).fetchall()} \n")

        query_11 = read_query('query_11.sql')
        print(f"11) {c.execute(query_11, (example_teacher_id, example_student_id,)).fetchone()} \n")

        query_12 = read_query('query_12.sql')
        print(f"12) {c.execute(query_12, (example_subject_id, example_group_id, )).fetchall()} \n")


except DatabaseError as err:
    logging.error(err)
except RuntimeError as err:
    logging.error(err)
except Exception as err:
    logging.error(err)
finally: conn.close()