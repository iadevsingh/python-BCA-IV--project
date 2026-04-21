# Data
data = [
    {"name": "Dev", "course": "BCA", "marks": 85},
    {"name": "Ram", "course": "BCA", "marks": 90},
    {"name": "Shyam", "course": "BBA", "marks": 78},
    {"name": "Amit", "course": "BCA", "marks": 88},
    {"name": "Ravi", "course": "BBA", "marks": 92}
]

print("Original Data:")
for d in data:
    print(d)

# ------------------ FILTERING ------------------
filtered = [d for d in data if d["marks"] > 85]

print("\nFiltered Data (marks > 85):")
for d in filtered:
    print(d)

# ------------------ GROUPING ------------------
group = {}

for d in data:
    course = d["course"]
    group.setdefault(course, []).append(d["marks"])

print("\nGrouped Data (Average marks by course):")
for course, marks in group.items():
    avg = sum(marks) / len(marks)
    print(course, ":", round(avg, 2))