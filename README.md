# Django Task Manager with Docker

A simple Task Manager API built with Django REST Framework, using a custom user model and JWT authentication, fully containerized with Docker and PostgreSQL.

---

## Features

- User registration and authentication (JWT)
- Create, read, update, delete tasks
- Tasks linked to authenticated users
- Filtering, searching, and ordering of tasks
- Dockerized setup for easy deployment
- PostgreSQL as the database backend

---

## Tech Stack

- Django
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- JWT Authentication (`djangorestframework-simplejwt`)
- django-filter

---

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup

1. Clone the repo:

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```
2. Create a .env file in the root directory and set your environment variables:
   
```
DB_NAME=task_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY=your-django-secret-key
```

3. Build and start containers:

```bash
docker-compose up --build
```
4. Apply migrations and create superuser:

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```
5.The API will be accessible at http://localhost:8000/

### API Endpoints
```
/api/register/ - User registration

/api/token/ - Obtain JWT token

/api/token/refresh/ - Refresh JWT token

/api/tasks/ - List and create tasks (authenticated)

/api/tasks/<id>/ - Retrieve, update, delete a task (authenticated)
```
### Filtering, Searching, Ordering Tasks
```
Filter by completion status:
/api/tasks/?is_completed=true

Search by title or description:
/api/tasks/?search=keyword

Order by due date or title:
/api/tasks/?ordering=due_date
or
/api/tasks/?ordering=-title
```
