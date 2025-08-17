-- Знайти список студентів у певній групі.

SELECT id, first_name, last_name
FROM students
WHERE group_id = ?;

