-- Знайти середній бал, який ставить певний викладач зі своїх предметів.

SELECT AVG(gr.grade) as avg_grade
FROM grades gr
JOIN subjects sub ON gr.subject_id = sub.id
WHERE sub.teacher_id = ?;

