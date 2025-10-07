class Student:
    def __init__(self):
        self.student_id = None
        self.student_name = ""
        self.city = ""
        self.marks1 = 0
        self.marks2 = 0
        self.marks3 = 0
        self.fee_per_month = 0.0
        self.is_eligible_for_scholarship = False

    # Setters
    def set_data(self, student_id, student_name, city, m1, m2, m3, fee, scholarship):
        self.student_id = student_id
        self.student_name = student_name
        self.city = city
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3
        self.fee_per_month = fee
        self.is_eligible_for_scholarship = scholarship

    # Getters
    def get_total_marks(self):
        return self.marks1 + self.marks2 + self.marks3

    def get_average(self):
        return self.get_total_marks() / 3

    def get_annual_fee(self):
        return self.fee_per_month * 12

    def get_result(self):
        return "pass" if all(mark > 60 for mark in [self.marks1, self.marks2, self.marks3]) else "fail"

# Test Script
s1 = Student()
s2 = Student()
s3 = Student()

s1.set_data(1, "Alice", "Chennai", 85, 90, 88, 1500.0, True)
s2.set_data(2, "Bob", "Delhi", 70, 65, 60, 1200.0, False)
s3.set_data(3, "Charlie", "Mumbai", 95, 92, 96, 1800.0, True)

students = [s1, s2, s3]

# Highest total marks
topper = max(students, key=lambda s: s.get_total_marks())
print("Topper:", topper.student_name)

# Lowest fee
lowest_fee = min(students, key=lambda s: s.fee_per_month)
print("Lowest Fee:", lowest_fee.student_name, lowest_fee.fee_per_month)

# Details
for s in students:
    print(f"{s.student_name}: Total={s.get_total_marks()}, Avg={s.get_average():.2f}, Result={s.get_result()}, Scholarship={s.is_eligible_for_scholarship}") 


