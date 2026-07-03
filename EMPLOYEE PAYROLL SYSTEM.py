 

employee_ids = [101, 102, 103]

employees = {
    101: {"name": "Rahul", "salary": 35000},
    102: {"name": "Priya", "salary": 90000},
    103: {"name": "Aman", "salary": 210000},
}


def allowance(salary):
    return salary * 0.10   

def deduction(salary):
    return salary * 0.05  

class Employee:
    def __init__(self, emp_id, name, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary + allowance(self.salary) - deduction(self.salary)

print("EMPLOYEE PAYROLL REPORT")
print("-" * 35)

for emp_id in employee_ids:
    try:
        emp = Employee(
            emp_id,
            employees[emp_id]["name"],
            employees[emp_id]["salary"]
        )

        final_salary = emp.calculate_salary()

        print("ID:", emp.emp_id)
        print("Name:", emp.name)
        print("Basic Salary:", emp.salary)
        print("Final Salary:", final_salary)
        print("-" * 35)

    except ValueError as e:
        print("Error:", e)