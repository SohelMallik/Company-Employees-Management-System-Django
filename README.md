# Company Employees Management System (Django)

## Overview

**Company Employees Management System** is a RESTful web application built using **Django** and **Django REST Framework (DRF)** for managing companies and their employees. The system provides APIs for creating, retrieving, updating, and deleting company and employee records while maintaining relationships between companies and their employees.

The project follows Django's MVC (Model-View-Template) architecture and leverages Django REST Framework's ViewSets, Serializers, and Router-based URL configuration to provide a clean and scalable API design.

---

## Features

### Company Management

* Create new companies
* Retrieve company details
* Update company information
* Delete companies
* List all companies

### Employee Management

* Add employees to companies
* Retrieve employee details
* Update employee records
* Delete employees
* List all employees

### Custom API Endpoint

* Retrieve all employees belonging to a specific company

Example:

```http

GET /api/v1/companies/1/employees/

```

Response:

```json
[
    {
        "employee_id": 2,
        "employee_name": "Sahil Mallik",
        "employee_email": "sahilmallik@gmail.com",
        "employee_phone": "3464535460",
        "employee_address": "Nandigram",
        "employee_salary": 34000.0,
        "about": "Sahil is Manager .",
        "position": "Other",
        "company": 1
    }
]
```

### Additional Features

* RESTful API architecture
* JSON-based request and response handling
* Database relationship management
* Django Admin integration
* Serializer-based data validation
* Exception handling for API requests

---

## Technology Stack

| Technology            | Purpose              |
| --------------------- | -------------------- |
| Python                | Programming Language |
| Django                | Web Framework        |
| Django REST Framework | REST API Development |
| MYSQL                | Default Database     |
| Django ORM            | Database Operations  |

---

## Project Structure

```text
companyapi/
│
├── manage.py
├── db.sqlite3
│
├── api/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializer.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
└── companyapi/
    ├── settings.py
    ├── urls.py
    ├── views.py
    ├── asgi.py
    ├── wsgi.py
    └── __init__.py
```

---

## Installation

### Prerequisites

Ensure the following are installed:

* Python 3.10+
* pip
* Git

### Clone Repository

```bash
git clone https://github.com/your-username/Company-Employees-Management-System-Django.git

cd Company-Employees-Management-System-Django
```

### Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install django
pip install djangorestframework
```

Or using requirements file:

```bash
pip install -r requirements.txt
```

---

## Database Setup

Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

---

## Running the Application

Start the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

---

## API Endpoints

### Companies

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| GET    | /companies/      | Get all companies |
| POST   | /companies/      | Create company    |
| GET    | /companies/{id}/ | Get company       |
| PUT    | /companies/{id}/ | Update company    |
| DELETE | /companies/{id}/ | Delete company    |

---

### Employees

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| GET    | /employees/      | Get all employees |
| POST   | /employees/      | Create employee   |
| GET    | /employees/{id}/ | Get employee      |
| PUT    | /employees/{id}/ | Update employee   |
| DELETE | /employees/{id}/ | Delete employee   |

---

### Custom Endpoint

Retrieve all employees associated with a company.

```http
GET /companies/{pk}/employees/
```

Example:

```http
GET /companies/1/employees/
```

---

## Sample API Usage

### Create Company

```json
POST /companies/

[
    {
        "company_id": 1,
        "company_name": "Star_Shop",
        "company_location": "Kolkata",
        "company_email": "shopstar@gmail.com",
        "about": "THis is the bigest Company From Kolkata.",
        "type": "IT"
    }
]
```

### Create Employee

```json
POST /employees/

[
    {
        "employee_id": 1,
        "employee_name": "Sohel Mallik",
        "employee_email": "sohel@gmail.com",
        "employee_phone": "4534674756",
        "employee_address": "Nandigram",
        "employee_salary": 40000.0,
        "about": "Sohel is Django Backend Developer.",
        "position": "HR",
        "company": 2
    }
]
```

---

## Configuration

Project configurations can be modified in:

```text
companyapi/settings.py
```

Common settings:

* Installed Applications
* Database Configuration
* Middleware
* Static Files
* REST Framework Settings
* Security Settings

Example database configuration:

```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'company',
        'USER': 'sohel',
        'PASSWORD': '2005',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## Testing

Run all tests:

```bash
python manage.py test
```

Run tests for a specific application:

```bash
python manage.py test api
```

---

## Error Handling

The project includes exception handling in custom endpoints.

Example:

```python
@action(detail=True, methods=['get'])
def employees(self, request, pk=None):
    try:
        company = Company.objects.get(pk=pk)
        employees = Employee.objects.filter(company=company)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=400
        )
```



## Contributing

Contributions are welcome.

### Steps

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Create a Pull Request

---

## License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this project under the terms of the license.

---

## Author

**Sohel Mallik**

B.Tech Computer Science & Engineering
Backend Developer | Django Developer | Software Engineering Enthusiast

GitHub:
https://github.com/SohelMallik

LinkedIn:
https://www.linkedin.com

---

## Acknowledgements

* Django Development Team
* Django REST Framework Team
* Open Source Community

---

### If you found this project useful, please consider giving it a ⭐ on GitHub.
