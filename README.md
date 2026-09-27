                 Employee Management System (EMS)
This is a simple Employee Management System built using Python, Django, HTML, CSS, and Bootstrap 5.
The project allows you to manage employees and keep track of their departments, roles, salary, bonus, phone number, and joining date.

Features
•	View Employees – View all employees in a table with their details.
•	Add Employee – Add a new employee by entering their basic information and selecting a department and role.
•	Remove Employee – Remove an employee from the system.
•	Search  –  Search employees by name, department or role.

Technologies Used
•	Python
•	Django
•	HTML5
•	CSS3
•	Bootstrap 5
•	SQLite
•	Git & GitHub

The project mainly contains:
•	models.py – Defines the Department, Role, and Employee database models.
•	views.py – Contains the logic for adding, viewing, removing, and filtering employees.
•	templates – Contains the HTML pages used for the website.
•	db.sqlite3 – SQLite database used for storing the project data.

How to Run the Project Locally
1. Clone the repository
      https://github.com/your-username/employee-management-system.git
2. Go to the project folder
     cd employee-management-system
3. Create a virtual environment
     python -m venv emp
4.Activate the virtual environment.
   Windows:
     emp\Scripts\activate
   macOS/Linux:
     source emp/bin/activate
5. Install Django
     pip install django
6. Apply migrations
     python manage.py makemigrations
     python manage.py migrate
7. Start the development server
     python manage.py runserver
8. Then open the URL shown in the terminal, usually:
     http://127.0.0.1:8000/
