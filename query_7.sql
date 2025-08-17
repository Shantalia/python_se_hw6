-- Знайти оцінки студентів у окремій групі з певного предмета.

SELECT s.id, s.first_name, s.last_name, gr.grade
FROM grades gr
JOIN students s ON gr.student_id = s.id
WHERE s.group_id = ? AND gr.subject_id = ?;

