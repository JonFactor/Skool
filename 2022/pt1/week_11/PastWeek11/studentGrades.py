student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}
for students in student_scores:
    if student_scores[students] >= 91:
        pf = "Outstanding"
    elif student_scores[students] >= 81:
        pf = "Exceeds Expectations"
    elif student_scores[students] >= 71:
        pf = "Acceptable"
    elif student_scores[students] <= 70:
        pf = "Fail"
    student_grades.__setitem__(students, pf) 
print(student_grades)