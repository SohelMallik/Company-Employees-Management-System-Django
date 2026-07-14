# 🚀 Company Employees Management System Api

A secure and scalable RESTful API built using **Django**, **Django REST Framework (DRF)**, **MySQL**, and **API Key Authentication** for managing companies and employees.

The project provides complete CRUD operations for companies and employees, company-employee relationship management, secure API access using **djangorestframework-api-key**, and JSON-based REST APIs following industry-standard backend development practices.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-6.0.5-green)
![DRF](https://img.shields.io/badge/DRF-3.17.1-red)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Overview

Company Employees Management System API is a secure RESTful web application built using Django, Django REST Framework (DRF), MySQL, and API Key Authentication.

The system provides complete CRUD operations for managing companies and employees while maintaining company-employee relationships through well-structured REST APIs.

### Key Capabilities

- Company Management APIs
- Employee Management APIs
- Company–Employee Relationship Management
- API Key Authentication
- JSON-Based API Communication
- Django Admin Integration
- Serializer-Based Data Validation
- Exception Handling

The project follows Django's **MVT (Model-View-Template)** architecture and leverages Django REST Framework's **ViewSets**, **Serializers**, **Routers**, and **Permission Classes** to build a clean, scalable, and maintainable backend system.

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


## 🛠 Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Django | Web Framework |
| Django REST Framework | REST API Development |
| MySQL | Database |
| Django ORM | Database Operations |
| API Key Authentication | API Security |
| Git | Version Control |
| GitHub | Source Code Management |

---

## 🔐 API Key Authentication

This project uses:

```bash
djangorestframework-api-key
```

to secure all API endpoints.

### Protected APIs

| Endpoint | Authentication |
|-----------|---------------|
| `/api/v1/companies/` | API Key Required |
| `/api/v1/employees/` | API Key Required |
| `/api/v1/companies/{id}/employees/` | API Key Required |

---

## Create API Key

### Install Package

```bash
pip install djangorestframework-api-key==3.1.0
```

### Add to INSTALLED_APPS

```python
INSTALLED_APPS = [
    ...
    "rest_framework",
    "rest_framework_api_key",
]
```

### Apply Migration

```bash
python manage.py migrate
```

### Generate API Key

Login to Django Admin:

```text
http://127.0.0.1:8000/admin/
```

Navigate:

```text
API Key Management
→ API Keys
→ Add API Key
```

Save the generated API key securely.

---

## Authentication Header

### Default Header

```http
Authorization: Api-Key YOUR_API_KEY
```

### Example

```http
GET /api/v1/companies/

Authorization: Api-Key YOUR_API_KEY
```

---

## API Security Workflow

```text
Client
   │
   │ API Key
   ▼
Django REST Framework
   │
   ▼
HasAPIKey Permission
   │
   ├── Valid Key → 200 OK
   └── Invalid Key → 403 Forbidden
```

---

## 📂 Project Structure

```text
Company-Employee-Management-System/
│
├── .github/
│
├── companyapi/
│   ├── manage.py
│   │
│   ├── api/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializer.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── __init__.py
│   │
│   └── companyapi/
│       ├── settings.py
│       ├── urls.py
│       ├── asgi.py
│       ├── wsgi.py
│       └── __init__.py
│
├── screenshots/
│
├── README.md
├── requirements.txt
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
└── SECURITY.md
```

---

## Installation

### Prerequisites

Ensure the following are installed:

- Python 3.10+
- pip
- Git
- MySQL Server

### Clone Repository

```bash
git clone https://github.com/SohelMallik/Company-Employees-Management-System-Django.git

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

## 📦 Requirements

```txt
Django==6.0.5
djangorestframework==3.17.1
djangorestframework-api-key==3.1.0
PyMySQL==1.2.0
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
## 🗄 Database Configuration

Example MySQL Configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'company',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
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
### Create a Company

```http
POST /api/v1/companies/
Content-Type: application/json
Authorization: Api-Key YOUR_API_KEY
```

```json
    {
        "company_id": 1,
        "company_name": "Star_Shop",
        "company_location": "Kolkata",
        "company_email": "shopstar@gmail.com",
        "about": "THis is the bigest Company From Kolkata.",
        "type": "IT"
    }
```

### Create an Employee

```http
POST /api/v1/employees/
Content-Type: application/json
Authorization: Api-Key YOUR_API_KEY
```

```json
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
```

---

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



---

## HTTP Status Codes

| Code | Description |
|------|-------------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

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

## 👨‍💻 Author

### Sohel Mallik

B.Tech Computer Science & Engineering  
Brainware University

Backend Developer | Django Developer | REST API Developer

### Skills

- Python
- Django
- Django REST Framework
- MySQL
- API Key Authentication
- Git & GitHub
- Data Structures & Algorithms

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
