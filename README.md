# 🎓 IN-TUT – Institute Management System

A scalable **full-stack Institute Management System** built with **Django** to digitize and streamline academic administration. The platform provides secure **Role-Based Access Control (RBAC)** for **HOD**, **Staff**, and **Students**, enabling efficient management of academic operations through a centralized web application.

---

## ✨ Key Features

- **Role-Based Access Control (RBAC)** for HOD, Staff, and Students
- **JWT Authentication** with secure REST APIs
- Complete **CRUD Operations** for Students, Staff, Branches, Subjects, and Academic Years
- **Attendance Management** with attendance reports
- **Leave Management** with approval workflow
- **Feedback & Notification** management system
- Advanced API capabilities including **Filtering, Searching, Ordering, and Pagination**
- Secure API testing using **Postman**

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| **Backend** | Python, Django, Django REST Framework |
| **Database** | SQLite |
| **Frontend** | HTML5, CSS3, Bootstrap, JavaScript |
| **Authentication** | JWT Authentication | Session Authentication
| **Deployment** | Docker, Docker Compose, Gunicorn, Nginx, AWS EC2 |
| **DevOps** | GitHub Actions (CI/CD) |
| **API Testing** | Postman |

---

## 🚀 Deployment

The application is containerized using **Docker** and deployed on **AWS EC2** with **Gunicorn** and **Nginx**, secured using **HTTPS (Let's Encrypt SSL)**. Continuous deployment is automated through **GitHub Actions (CI/CD)**.

---

## 🔗 REST API Features

- RESTful APIs using Django REST Framework
- JWT Authentication & Authorization
- Role-Based Permissions
- CRUD Operations
- Filtering
- Searching
- Ordering
- Pagination

---

⚙️ Getting Started
1. Clone the repository
git clone https://github.com/priyankakush8890/institute-management-system.git
cd institute-management-system
2. Install dependencies
It is recommended to create and activate a virtual environment first.
Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Linux / macOS
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Apply database migrations
python manage.py migrate
4. Start the development server
python manage.py runserver
Open http://127.0.0.1:8000 in your browser.
Run with Docker
Build and start the application using Docker Compose:
docker compose up --build
In the EC2 deployment, the host port is mapped to 127.0.0.1:8001 and the container runs Gunicorn on port 8000. Local Docker port mapping may differ depending on your docker-compose.yml configuration.


🌐 Live Demo
Live Website: https://ims-priyanka.duckdns.org
