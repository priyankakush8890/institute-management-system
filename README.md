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
| **Authentication** | JWT Authentication |
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

## ⚙️ Getting Started

```bash
git clone https://github.com/yourusername/IN-TUT.git
cd IN-TUT

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

### Run with Docker

```bash
docker compose up --build
```



