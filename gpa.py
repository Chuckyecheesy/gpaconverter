import math

def percentage_to_gpa(percent):
    """Convert percentage (0-100) to 4.0 GPA"""
    return percent / 100 * 4

def scale12_to_gpa(gpa_12):
    """Convert 12-point scale to 4.0 GPA"""
    return gpa_12 / 12 * 4

def scale5_to_gpa(gpa_5):
    """Convert 5-point scale to 4.0 GPA"""
    return gpa_5 / 5 * 4

def letter_grade_to_gpa(grade):
    """Convert letter grade to 4.0 GPA"""
    grade_index = [
        ["A+", 4.0], ["A", 4.0], ["A-", 3.7],
        ["B+", 3.3], ["B", 3.0], ["B-", 2.7],
        ["C+", 2.3], ["C", 2.0], ["C-", 1.7],
        ["D+", 1.3], ["D", 1.0], ["D-", 0.7],
        ["F", 0.0]
    ]
    grade = grade.upper()
    for pair in grade_index:
        if grade == pair[0]:
            return pair[1]
    return None  # if grade not found
