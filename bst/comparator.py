from abc import ABC, abstractmethod
from student import Student


# Strategy Pattern Implementation
# Strategy Interface
class ComparatorStrategy(ABC):
    @abstractmethod
    def compare(self, student1, student2):
        # Define the comparison method signature.
        # Concrete strategies will implement this method to compare two students based on specific attributes.
        pass

# Concrete Strategy: Compare students by redId
class ByRedIdComparator(ComparatorStrategy):
    def compare(self, student1: Student, student2: Student):
        # Compare two students by their red ID.
        # Returns a positive, zero, or negative integer depending on the difference between red IDs.
        return student1.red_id - student2.red_id 

# Concrete Strategy: Compare students by Name
class ByNameComparator(ComparatorStrategy):
    def compare(self, student1: Student, student2: Student):
        # Compare two students by their last and first names.
        # If last names are identical, compare by first name.
        # Returns 1 if student1's name comes after student2's name lexicographically, -1 if before, and 0 if identical.
        if student1.last_name == student2.last_name:
            return (student1.first_name > student2.first_name) - (student1.first_name < student2.first_name)
        return (student1.last_name > student2.last_name) - (student1.last_name < student2.last_name)

# Concrete Strategy: Compare students by GPA
class ByRoundedGPAComparator(ComparatorStrategy):
    def compare(self, student1: Student, student2: Student):
        # Compare two students by their rounded GPA values.
        # If the rounded GPA values are the same, fall back to comparing by red ID.
        # Returns a positive, zero, or negative integer based on GPA comparison.
        gpa_diff = round(student1.gpa) - round(student2.gpa)
        if gpa_diff == 0:
            return student1.red_id - student2.red_id
        return gpa_diff