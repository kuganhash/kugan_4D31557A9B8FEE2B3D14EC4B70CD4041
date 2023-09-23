class Student:
    def _init_(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Sample student data as instances of the Student class
student_data = [
    Student("Alice", 101, 3.8),
    Student("Bob", 102, 3.5),
    Student("Charlie", 103, 3.9),
    Student("David", 104, 3.2),
    Student("Eve", 105, 3.7),
]

# Sort the student data by CGPA in descending order
sorted_student_data = sorted(student_data, key=lambda x: x.cgpa, reverse=True)

# Print the sorted data
for student in sorted_student_data:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")