-- Оцінки студентів у певній групі з певного предмета на останньому занятті.

SELECT s.id, s.first_name, s.last_name, g.grade, g.subject_id, g.date_of_grade
FROM grades g
         JOIN students s ON s.id = g.student_id
WHERE g.subject_id = ?
  AND s.group_id = ?
  AND g.date_of_grade = (SELECT MAX(gr.date_of_grade) FROM grades gr WHERE gr.subject_id = g.subject_id);

