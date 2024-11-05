class Student:
    def __init__(self, first_name, last_name, red_id, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.red_id = red_id
        self.gpa = gpa

    def __repr__(self):
        return f"Student({self.first_name} {self.last_name}, ID: {self.red_id}, GPA: {self.gpa})"
    
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_red_id(self):
        return self.red_id

    def get_gpa(self):
        return self.gpa


class Comparator:
    @staticmethod
    def by_red_id(student1, student2):
        return student1.red_id - student2.red_id

    @staticmethod
    def by_name(student1, student2):
        if student1.last_name == student2.last_name:
            return (student1.first_name > student2.first_name) - (student1.first_name < student2.first_name)
        return (student1.last_name > student2.last_name) - (student1.last_name < student2.last_name)

    @staticmethod
    def by_rounded_gpa(student1, student2):
        gpa_diff = round(student1.gpa) - round(student2.gpa)
        if gpa_diff == 0:
            return student1.red_id - student2.red_id
        return gpa_diff
