from sqlite3_connector import cursor
from queries import read_query

# Всі таблиці
query_for_data_deletion = read_query('data_deletion.sql')
cursor.execute(query_for_data_deletion)