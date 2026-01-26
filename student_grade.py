total_students = 0

def get_marks():
   
    total = 0
    for i in range(1, 6):
        while True:
            mark = int(input(f"Enter marks for subject {i} (0-100): "))
            if 0 <= mark <= 100:
                break
            else:
                print("Invalid marks! Enter again.")
        total += mark
    return total

def grade_calculator(total_marks):
    avg = total_marks / 5

    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def main():
    global total_students
    total_students += 1

    name = input("Enter student name: ")
    total_marks = get_marks()
    grade = grade_calculator(total_marks)

    print("\n--- Result ---")
    print("Name:", name)
    print("Total Marks:", total_marks)
    print("Grade:", grade)

   
    num = int(input("\nEnter a number to find factorial: "))
    print("Factorial:", factorial(num))

if __name__ == "__main__":
    main()
   student_grade.py