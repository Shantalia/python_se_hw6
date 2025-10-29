from utils.date_adapter import sqlite3

# Створення з'єднання з базою даних
conn = sqlite3.connect('db_hw_6.sqlite')
cursor = conn.cursor()