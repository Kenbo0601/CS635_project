# Student Class 
class Student:
    def __init__(self, first_name, last_name, red_id, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.red_id = red_id
        self.gpa = gpa

    def __repr__(self):
        return f"Student({self.first_name} {self.last_name}, ID: {self.red_id}, GPA: {self.gpa})"
