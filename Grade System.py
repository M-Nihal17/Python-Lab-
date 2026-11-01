# User-defined functions
def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks)

def find_highest(marks):
    return max(marks)

def find_lowest(marks):
    return min(marks)

def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 40:
        return 'D'
    else:
        return 'F'

students = []
  
n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    marks = list(map(int, input(f"Enter marks of {name} (separated by space): ").split()))
    
    total = calculate_total(marks)
    avg = calculate_average(marks)
    highest = find_highest(marks)
    lowest = find_lowest(marks)
    grade = get_grade(avg)
    
    students.append({
        'name': name,
        'marks': marks,
        'total': total,
        'average': avg,
        'grade': grade,
        'highest': highest,
        'lowest': lowest
    })

students_sorted = sorted(students, key=lambda x: x['total'], reverse=True)

print("\n--- Student Performance Report (Sorted by Total) ---")
for s in students_sorted:
    print(f"\nName: {s['name']}")
    print(f"Marks: {s['marks']}")
    print(f"Total: {s['total']}, Average: {s['average']:.2f}")
    print(f"Highest: {s['highest']}, Lowest: {s['lowest']}")
    print(f"Grade: {s['grade']}")
