-- Знайти які курси читає певний викладач.

SELECT name
FROM subjects
WHERE teacher_id = ?;

