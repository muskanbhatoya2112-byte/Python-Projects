# Student Result Management System

students = {
    "AMAAN": [81, 70, 98],
    "DUREE": [62, 95, 81],
    "RABIYA": [88, 89, 95]
}
topper = ""
highest_avg = 0

for name, marks in students.items():

    avg = sum(marks) / len(marks)

    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "D"

    print("Student:", name)
    print("Marks:", marks)
    print("Average:", avg)
    print("Grade:", grade)
    print()

    if avg > highest_avg:
        highest_avg = avg
        topper = name

print("Topper:", topper)
print("Highest Average:", highest_avg)


 
