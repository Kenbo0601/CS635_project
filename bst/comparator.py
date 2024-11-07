from abc import ABC, abstractmethod
from student import Student

# Stategy Pattern Implementation 
# Starategy Interface 
class ComparatorStrategy(ABC):
    @abstractmethod
    def compare(self, student1, student2):
        pass

# Concrete Strategy: Compare students by redId 
class ByRedIdComarator(ComparatorStrategy):
    def compare(self, student1: Student, student2: Student):
        return student1.red_id - student2.red_id 

# Concrete Strategy: Compare students by Name
class ByNameComparator(ComparatorStrategy):
    def compare(self, student1: Student, student2: Student):
        if student1.last_name == student2.last_name:
            return (student1.first_name > student2.first_name) - (student1.first_name < student2.first_name)
        return (student1.first_name > student2.first_name) - (student1.first_name < student2.first_name)

# Concrete Strategy: Compare students by GPA
class ByRoundedGPAComparator(ComparatorStrategy):
    def compare(self, student1: Student, student2: Student):
        gpa_diff = round(student1.gpa) - round(student2.gpa)
        if gpa_diff == 0:
            return student1.red_id - student2.red_id
        return gpa_diff