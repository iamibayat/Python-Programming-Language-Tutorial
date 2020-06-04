from student import Student

student1 = Student("Amir", 1631050, "CSE", 3.3, False)
student2 = Student("Hamza", 1631030, "Business", 3.5, True)

print(student1.stu_id)
print(student1.is_on_probation)
print("\n")

print(student1.on_honor_role())
print(student2.on_honor_role())
