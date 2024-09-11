# Student Course Management System

The Student Course Management System is a comprehensive web application developed using Python and Django, designed to facilitate efficient management of courses, students, and enrollments for educational institutions. This system provides various features to streamline the process of course administration and student engagement.

## Features
**User Authentication and Authorization**:
Implemented roles for administrators, instructors, and students.
Utilizes Django’s built-in authentication system for secure login and role-based access.

**Course Management**:
Administrators and instructors can create, update, and delete courses.
Courses can have multiple modules accessible to students based on their enrollment status.

**Student Enrollment**:
Students can browse available courses and enroll with an intuitive interface.
Tracks enrollment status and course progress with validation checks.

**Database Integration**:
Uses PostgreSQL for managing data, including user profiles, course details, and enrollments.
Features optimized queries and performance improvements for handling large datasets.

**RESTful API Development**:
Developed a RESTful API using Django Rest Framework (DRF) for third-party integration.
API supports CRUD operations for courses and enrollments.


## Installation
   
1. Clone the Repository:
2. Navigate to the Project Directory : cd student-course-management-system
3. Create a Virtual Environment : python -m venv env
4. Activate the Virtual Environment : .\env\Scripts\activate
5. Install Dependencies : pip install -r requirements.txt
6. Apply Migrations : python manage.py migrate
7. Create a Superuser : python manage.py createsuperuser
8. Run the Development Server : python manage.py runserver

   ## Access the application at http://127.0.0.1:8000/

