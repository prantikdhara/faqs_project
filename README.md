# faqs_project
Multilingual FAQ System

Overview

This project is a Django-based FAQ system that supports multilingual content. It allows users to add FAQs with rich-text answers, retrieve them via a REST API, and automatically translate them into different languages. Caching with Redis ensures fast responses.

Features

Django Models: Stores FAQs with multilingual support.

WYSIWYG Editor: Uses django-ckeditor for rich-text formatting.

REST API: Fetch FAQs in different languages using query parameters.

Caching with Redis: Improves performance by storing translated FAQs.

Automated Translations: Uses Google Translate API.

Admin Panel: Manage FAQs from the Django Admin interface.

Unit Tests: Ensures API correctness and model functionality.

PEP8 Compliance: Code follows best practices.

Installation

Prerequisites

Ensure you have the following installed:

Python (>=3.8)

PostgreSQL (or SQLite for development)

Redis

Docker (optional for deployment)

Clone Repository

git clone https://github.com/prantikdhara/faqs_project.git
cd faqs_project

Create Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies

pip install -r requirements.txt

Configure Environment Variables

Create a .env file in the root directory:

SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3  # Change for PostgreSQL
REDIS_URL=redis://127.0.0.1:6379/1

Apply Migrations

python manage.py makemigrations
python manage.py migrate

Create Superuser

python manage.py createsuperuser

Run Server

python manage.py runserver

API Usage

Fetch FAQs (Default: English)

curl http://localhost:8000/api/faqs/

Fetch FAQs in Hindi

curl http://localhost:8000/api/faqs/?lang=hi

Fetch FAQs in Bengali

curl http://localhost:8000/api/faqs/?lang=bn

Running Tests

pytest

Deployment with Docker

Build and Run Docker Containers

docker-compose up --build

Contribution Guidelines

Fork the repository.

Create a feature branch: git checkout -b feature-name

Commit your changes following conventional commits:

git commit -m "feat: add FAQ API endpoint"

