# Student-Course-Management
The program is a Python-based student management system that conencts a MySQL database called SchoolDB to contain student course information. The program allows a user to add a student, add a course, enroll a student in a course, and display a student's enrollment. 

# Running
1. Make sure MySQL Server is installed and running.
2. Install the MySQL Connector package by running: pip install mysql-connector-python

3. Create the SchoolDB database and the Students, Courses, and Enrollments tables using the SQL statements provided with this project.

4. Open the Python file and change the database connection information:
host="localhost"
user="root"
password="your_password"
database="SchoolDB"
*Replace "your_password" with your actual MySQL password.*
