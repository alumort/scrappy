# Scrappy

A work-in-progress scalable web scraping platform built with **Django** and **Django REST Framework** that allows extracting, storing, and exposing web data through a RESTful API.

This project focuses on backend development practices such as API design, database management, asynchronous processing, containerization, and automated data collection.

---

## Features

- Soon
---

# Tech Stack

## Backend

- Python 3.12
- Django
- Django REST Framework
- Redis
- Celery

## Infrastructure

- Docker
- Docker Compose
- Linux environment

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

cd webscraper
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
webscraper/
│
├── apps/
│   ├── scraper/
│   ├── api/
│   └── core/
│
├── config/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── manage.py
└── README.md
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
