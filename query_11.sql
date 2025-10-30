-- Середній бал, який певний викладач ставить певному студентові.

SELECT AVG(gr.grade) as avg_grade
FROM grades gr
INNER JOIN subjects sub ON gr.subject_id = sub.id
WHERE sub.teacher_id = ? AND gr.student_id = ?;
