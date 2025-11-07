def calculate_grade(marks):
  if marks >= 90:
    return "A"
  elif marks >= 80:
    return "B"
  elif marks >= 70:
    return "C"
  elif marks >= 60:
    return "D"
  else:
    return "Fail"
student_marks = int(input("Enter the student's marks: "))
  if 0 <= student_marks <= 100:
    grade = calculate_grade(student_marks)
    print(f"The student's grade is: {grade}")
  else:
    print("Invalid marks. Please enter a value between 0 and 100.")
