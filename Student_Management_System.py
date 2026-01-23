students = []

def add_student():
    roll = int(input("Enter roll number: "))

    if roll <= 0:
        print("Roll number must be positive.")
        return

    for s in students:
        if s["roll"] == roll:
            print("Roll number already exists.")
            return

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully.")


def view_students():
    if not students:
        print("No student records found.")
        return

    for s in students:
        print("----------------------")
        print("Roll No:", s["roll"])
        print("Name:", s["name"])
        print("Age:", s["age"])
        print("Course:", s["course"])
        print("Marks:", s["marks"])
    print("----------------------")


def search_student():
    roll = int(input("Enter roll number to search: "))
    for s in students:
        if s["roll"] == roll:
            print("Student found:")
            print(s)
            return
    print("Student not found.")


def update_student():
    roll = int(input("Enter roll number to update: "))
    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter new name: ")
            s["age"] = int(input("Enter new age: "))
            s["course"] = input("Enter new course: ")
            s["marks"] = float(input("Enter new marks: "))
            print("Student updated successfully.")
            return
    print("Student not found.")


def delete_student():
    roll = int(input("Enter roll number to delete: "))
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully.")
            return
    print("Student not found.")


while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting program. Thank you.")
        break
    else:
        print("Invalid choice. Try again.")
