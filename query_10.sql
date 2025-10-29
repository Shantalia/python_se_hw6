-- Список курсів, які певному студенту читає певний викладач.

SELECT DISTINCT sub.name
FROM grades gr
JOIN subjects sub ON gr.subject_id = sub.id
WHERE gr.student_id = ? AND sub.teacher_id = ?;

