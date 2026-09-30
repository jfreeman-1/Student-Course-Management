import mysql.connector

# Connect to SchoolDB
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="SchoolDB"
)

cursor = db.cursor()


def add_student():
    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    major = input("Enter student major: ")

    sql = """
        INSERT INTO Students (student_id, name, age, major)
        VALUES (%s, %s, %s, %s)
    """

    try:
        cursor.execute(sql, (student_id, name, age, major))
        db.commit()
        print("Student added successfully.")
    except mysql.connector.Error as err:
        print("Error:", err)
        db.rollback()


def add_course():
    course_id = int(input("Enter course ID: "))
    course_name = input("Enter course name: ")
    credits = int(input("Enter number of credits: "))

    sql = """
        INSERT INTO Courses (course_id, course_name, credits)
        VALUES (%s, %s, %s)
    """

    try:
        cursor.execute(sql, (course_id, course_name, credits))
        db.commit()
        print("Course added successfully.")
    except mysql.connector.Error as err:
        print("Error:", err)
        db.rollback()


def enroll_student():
    enrollment_id = int(input("Enter enrollment ID: "))
    student_id = int(input("Enter student ID: "))
    course_id = int(input("Enter course ID: "))
    grade = input("Enter grade: ")

    sql = """
        INSERT INTO Enrollments
        (enrollment_id, student_id, course_id, grade)
        VALUES (%s, %s, %s, %s)
    """

    try:
        cursor.execute(sql, (enrollment_id, student_id, course_id, grade))
        db.commit()
        print("Student enrolled successfully.")
    except mysql.connector.Error as err:
        print("Error:", err)
        db.rollback()


def show_enrollments():
    student_id = int(input("Enter student ID: "))

    sql = """
        SELECT 
            Students.name,
            Courses.course_name,
            Courses.credits,
            Enrollments.grade
        FROM Enrollments
        JOIN Students
            ON Enrollments.student_id = Students.student_id
        JOIN Courses
            ON Enrollments.course_id = Courses.course_id
        WHERE Students.student_id = %s
    """

    cursor.execute(sql, (student_id,))
    results = cursor.fetchall()

    if results:
        print("\nStudent Enrollments:")
        print("--------------------")

        for name, course, credits, grade in results:
            print("Student:", name)
            print("Course:", course)
            print("Credits:", credits)
            print("Grade:", grade)
            print()
    else:
        print("No enrollments found for this student.")


# Main menu
while True:
    print("\n===== Student-Course Management System =====")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student in Course")
    print("4. Show Student's Enrollments")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        add_course()

    elif choice == "3":
        enroll_student()

    elif choice == "4":
        show_enrollments()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")


# Close database connection
cursor.close()
db.close()
