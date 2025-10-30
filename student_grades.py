student_grades = {"Alice": [88, 92, 78.3], "Bob": [74.33, 80, 85], "Charlie":
[95, 89, 90]}
for student, grades in student_grades.items():
    average = sum(grades) / len(grades)

  
print(f"{student}'s average grade: {average:.2f}")

all_grades = []
for grades in student_grades.values():
    all_grades.extend(grades)

highest = max(all_grades)
lowest = min(all_grades)

print(f"\nHighest grade in class: {highest}")
print(f"Lowest grade in class: {lowest}")
