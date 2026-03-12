"""1.Student Grade Management System 
Program that records, updates, and deletes student grades. 
Handle exceptions like invalid student ID, empty grade inputs, and type 
mismatches. """
class StudentGradeManagement:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, grade):
        if not student_id or not grade:
            raise ValueError("Student ID and grade cannot be empty.")
        if not isinstance(student_id, str) or not isinstance(grade, (int, float)):
            raise TypeError("Student ID must be a string and grade must be a number.")
        self.students[student_id] = grade

    def update_grade(self, student_id, new_grade):
        if student_id not in self.students:
            raise KeyError("Student ID does not exist.")
        if not isinstance(new_grade, (int, float)):
            raise TypeError("Grade must be a number.")
        self.students[student_id] = new_grade

    def delete_student(self, student_id):
        if student_id not in self.students:
            raise KeyError("Student ID does not exist.")
        del self.students[student_id]

    def get_grade(self, student_id):
        if student_id not in self.students:
            raise KeyError("Student ID does not exist.")
        return self.students[student_id]
# Example usage
if __name__ == "__main__":
    grade_manager = StudentGradeManagement()
    try:
        grade_manager.add_student("S001", 85)
        grade_manager.add_student("S002", 90)
        print(grade_manager.get_grade("S001"))  # Output: 85
        grade_manager.update_grade("S001", 88)
        print(grade_manager.get_grade("S001"))  # Output: 88
        grade_manager.delete_student("S002")
        print(grade_manager.get_grade("S002"))  # This will raise an exception
    except (ValueError, TypeError, KeyError) as e:
        print("Error:", e)

        