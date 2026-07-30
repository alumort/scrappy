# Scrappy

A web scraping API built with Django and Django REST Framework.

Scrappy is designed to collect information from websites, process the extracted data, and expose it through a REST API. The project follows a service-oriented architecture, making it easy to extend with new scrapers.

---

## Features

- Django REST Framework
- Dockerized development environment
- PostgreSQL database
- Modular scraper architecture
- BeautifulSoup parsing
- Background tasks support (Celery - upcoming)
- Multi-site scraping support (planned)
---

# Tech Stack

- Python 3.12
- Django
- Django REST Framework
- PostgreSQL
- Docker
- BeautifulSoup4
- Requests
- Celery (planned)
- Redis (planned)

---

# Architecture Overview

```
                    ┌──────────────┐
                    │  External    │
                    │  Websites    │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  Scraper     │
                    │  Engine      │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ PostgreSQL   │
                    │  Database    │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ Django REST  │
                    │     API      │
                    └──────────────┘
```

---

# Installation

## Clone the repository

```bash
git clone https://github.com/alumort/scrappy.git

cd scrappy
```

---

## Environment Variables

Create a `.env` file:

```env
DEBUG=True

POSTGRES_DB=webscraper
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

REDIS_HOST=redis
REDIS_PORT=6379
```

---

# Running with Docker

Build and start the containers:

```bash
docker compose up --build
```

Run migrations:

```bash
docker compose exec web python manage.py migrate
```

Create a superuser:

```bash
docker compose exec web python manage.py createsuperuser
```

The API will be available at:

```
http://localhost:8000/
```

---

# API Endpoints

Example endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/products/` | List scraped products |
| GET | `/api/products/{id}/` | Retrieve product details |
| POST | `/api/scrapers/run/` | Start a scraping task |

---

# Scraping Workflow

The scraping process works as follows:

1. A scraping task is created.
2. The scraper collects information from the target website.
3. The extracted data is cleaned and validated.
4. The information is stored in PostgreSQL.
5. The API exposes the collected data.

---

# Background Tasks

Celery is used to execute scraping operations asynchronously.

Workflow:

```
User Request
      |
      ▼
Django API
      |
      ▼
Celery Task
      |
      ▼
Scraper Worker
      |
      ▼
Database
```

---

# Project Structure

```

```

---

# Future Improvements

- [ ] Add support for multiple scraping providers
- [ ] Implement authentication with JWT
- [ ] Add scraper dashboard
- [ ] Add automated tests

---

# Learning Goals

This project is being created to practice:

- Backend architecture design
- REST API development
- Web scraping techniques
- Asynchronous processing
- Database optimization
- Docker containerization
- Production-ready backend practices

---

# License

This project is licensed under the MIT License.
