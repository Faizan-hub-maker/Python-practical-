print("UIN: 251A029")
print("Date: 09-02-26")

Student = {}
n = int(input("Enter the number of students: "))

for _ in range(n):
    name = input("Name: ")
    # Creating the record
    Student[name] = {
        "UIN": input("Enter UIN: "), 
        "Grade": input("Enter Grade: ")
    }

print(Student)

u = input("Update Attendance for: ")
if u in Student:
    # Updating/Adding the attendance field
    Student[u]["Attendance"] = input("New Attendance: ")
