#Teachers enter marks, calculate GPA
class Student:
    def __init__(self):
        self.name = ""
        self.marks = []
        self.percentage = 0.0
        self.cgpa = 0.0
    def input_details(self):
        self.name = input("Enter student name: ")
        num_subjects = int(input("Enter number of subjects: "))
        for i in range(num_subjects):
            mark = float(input(f"Enter marks for subject {i+1}: "))
            self.marks.append(mark)
        self.calculate_percentage()
        self.calculate_cgpa()

    def calculate_percentage(self):
        total_marks = sum(self.marks)
        num_subjects = len(self.marks)
        if num_subjects > 0:
            self.percentage = (total_marks / (num_subjects * 100)) * 100

    def calculate_cgpa(self):
        total_grade_points = sum(mark / 25 for mark in self.marks)  # Assuming marks are out of 100
        num_subjects = len(self.marks)
        if num_subjects > 0:
            self.cgpa = total_grade_points / num_subjects
    def display_result(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Percentage: {self.percentage:.2f}%")
        print(f"CGPA: {self.cgpa:.2f}")
# Main function to demonstrate the result management system
if __name__ == "__main__":
    while True: 
        student = Student()
        student.input_details()
        student.display_result()
        cont = input("Do you want to enter details for another student? (yes/no): ")
        if cont.lower() != 'yes':
            break
