def authenticate_teacher():
    username = ["teacher"]
    password = "123"
    max_attempts = 3

    for attempt in range(max_attempts):
        u = input("Enter a username: ")
        p = input("Enter the password: ")

        if (u in username) and (p == password):
            print("Login successful")
            return True
        else:
            print("Login failed")

    print("You've used all your attempts. Access denied.")
    return False

def main():
    students_db = {}  # Use a dictionary to store student records
    attendance_db = {}  # Use a dictionary to store attendance records

    while True:
        print("Student Attendance Management System")
        print("1. Student Login")
        print("2. Teacher Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':  # Student Login
            student_id = input("Enter your Student ID: ")
            student_record = students_db.get(student_id)  # Use dictionary.get() to safely access student records

            if student_record:
                print("Date       | Attendance")
                print("-" * 25)
                for date, attendance in attendance_db.items():
                    student_attendance = attendance.get(student_id, "N/A")
                    print(f"{date} | {student_attendance}")
            else:
                print("Student not found.")

        elif choice == '2':  # Teacher Login
            if not authenticate_teacher():
                continue
            while True:
                print("Teacher Menu")
                print("1. Add Student Record")
                print("2. View Student Records")
                print("3. Update Student Record")
                print("4. Delete Student Record")
                print("5. Mark Attendance")
                print("6. View Attendance Records")
                print("7. Log out")

                teacher_choice = input("Enter your choice: ")

                if teacher_choice == '1':  # Add Student Record
                    student_id = input("Enter Student ID: ")
                    if student_id in students_db:
                        print("Student ID already exists. Please enter a unique ID.")
                    else:
                        name = input("Enter Student Name: ")
                        age = input("Enter Student Age: ")
                        branch = input("Enter Student Branch: ")
                        year = input("Enter Student Year")
                        students_db[student_id] = {'name': name, 'age': age, 'branch': branch, 'year': year}
                        print("Student added successfully!")

                elif teacher_choice == '2':  # View Student Records
                    if not students_db:
                        print("No student records found.")
                    else:
                        print("Student ID | Name      | Age | Branch  | Year")
                        print("-" * 40)
                        for student_id, student_info in students_db.items():
                            print(f"{student_id:^10} | {student_info['name']:^10} | {student_info['age']:^3} | {student_info['branch']:^5}  |  {student_info['year']:^5}")


                elif teacher_choice == '3':  # Update Student Record
                    student_id = input("Enter Student ID to update: ")
                    if student_id in students_db:
                        print(f"Updating information for {students_db[student_id]['name']}")
                        students_db[student_id]['name'] = input("Enter new Name: ")
                        students_db[student_id]['age'] = input("Enter new Age: ")
                        students_db[student_id]['branch'] = input("Enter new Branch: ")
                        students_db[student_id]['year'] = input("Enter new Year: ")
                        print("Student information updated!")
                    else:
                        print("Student not found.")

                elif teacher_choice == '4':  # Delete Student Record
                    student_id = input("Enter Student ID to delete: ")
                    if student_id in students_db:
                        del students_db[student_id]
                        print("Student deleted!")
                    else:
                        print("Student not found.")

                elif teacher_choice == '5':  # Mark Attendance
                    date = input("Enter Date (YYYY-MM-DD): ")
                    if date in attendance_db:
                        print(f"Attendance is already marked for {date}.")
                    else:
                        print("Marking attendance for students...")
                        attendance_db[date] = {}
                        for student_id in students_db:
                            attendance = input(f"Is {students_db[student_id]['name']} present? (Y/N): ").upper()
                            attendance_db[date][student_id] = attendance
                        print("Attendance marked successfully!")

                elif teacher_choice == '6':  # View Attendance Records
                    student_id = input("Enter Student ID to view attendance: ")
                    if student_id in students_db:
                        print("Date       | Attendance")
                        print("-" * 25)
                        for date, attendance_info in attendance_db.items():
                            attendance = attendance_info.get(student_id, "N/A")
                            print(f"{date} | {attendance}")
                    else:
                        print("student not found")

                elif teacher_choice == '7':  # Log out
                    print("Logging out from teacher account.")
                    break

                else:
                    print("Invalid choice. Please select a valid option.")

        elif choice == '3':  # Exit
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()