# Student Class
class Student:
    def __init__(self, first_name, last_name, red_id, gpa):
        # Initialize a Student object with the following attributes:
        # - first_name: The student's first name.
        # - last_name: The student's last name.
        # - red_id: A unique identifier for the student.
        # - gpa: The student's Grade Point Average (GPA).
        self.first_name = first_name
        self.last_name = last_name
        self.red_id = red_id
        self.gpa = gpa

    def __repr__(self):
        # Provide a readable string representation of the Student object
        # Useful for debugging and displaying student information
        return f"Student({self.first_name} {self.last_name}, ID: {self.red_id}, GPA: {self.gpa})"

