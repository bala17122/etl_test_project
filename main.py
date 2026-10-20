employees = [
    {"name": "Arun", "department": "IT", "salary": 75000},
    {"name": "Priya", "department": "HR", "salary": 55000},
    {"name": "Kumar", "department": "IT", "salary": 85000}
]

# Extract
data = employees

# Transform
it_employees = [
    emp for emp in data
    if emp["department"] == "IT"
]

# Load / Display
for employee in it_employees:
    print(employee)