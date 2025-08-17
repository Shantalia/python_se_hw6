-- Знайти список курсів, які відвідує студент.

SELECT DISTINCT sub.name
FROM grades gr
JOIN subjects sub ON gr.subject_id = sub.id
WHERE gr.student_id = ?;

