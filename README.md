# Employee Management System

A web-based Employee Management System developed using **Python, Django, HTML, CSS, and Bootstrap 5**.

This project provides a user-friendly interface for managing employee records. It demonstrates Django's Model-View-Template (MVT) architecture, database operations, form handling, and backend development.

## Features

- **Add Employees:** Create new employee records.
- **View Employees:** Display employee information.
- **Remove Employees:** Delete employee records from the system.
- **Search Employees:** Find employees using the application's search functionality.
- **Responsive Interface:** User interface developed using HTML, CSS, and Bootstrap 5.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| HTML | Webpage structure |
| CSS | Styling |
| Bootstrap 5 | Responsive user interface |
| SQLite | Development database |

## Project Structure

The project follows Django's Model-View-Template (MVT) architecture.

- **Models:** Define employee data and database structure.
- **Views:** Handle application logic and HTTP requests.
- **Templates:** Render the user interface.
- **URLs:** Map requests to application views.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/dahiya-03/employee-management-system.git
```

### 2. Navigate to the Project Directory

```bash
cd employee-management-system
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

If the repository includes `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Otherwise, install the dependencies documented for the project before continuing.

### 6. Apply Database Migrations

Run the following command from the directory containing `manage.py`:

```bash
python manage.py migrate
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

http://127.0.0.1:8000/

## Screenshots

Screenshots of the application's pages will be added here.

## Future Improvements

- PostgreSQL database integration
- User authentication and authorization
- Employee record editing
- Deployment to a cloud hosting platform

## Author

**GitHub:** [dahiya-03](https://github.com/dahiya-03)
