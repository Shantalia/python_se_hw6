-- Знайти середній бал у групах з певного предмета.

SELECT g.name, AVG(gr.grade) as avg_grade
FROM grades gr
JOIN students s ON gr.student_id = s.id
JOIN groups g ON s.group_id = g.id
WHERE gr.subject_id = ?
GROUP BY g.name;

