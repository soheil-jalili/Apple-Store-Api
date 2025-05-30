# Apple Store API Shop

This is a RESTful API built with Django and Django REST Framework for managing an Apple Store-like e-commerce backend.

## Features

- Product categories and listing
- Slider products for homepage
- Best-selling and featured products
- Apple Watch-specific product filtering
- Poster management (main and footer banners)
- Fully structured API responses for front-end integration

## Technologies

- Python
- Django
- Django REST Framework (DRF)
- SQLite / PostgreSQL (switchable)
- Git version control

## Getting Started

1. Clone the repository:
git clone https://github.com/soheil-jalili/Apple-Store-Api.git
2. Install dependencies:
pip install -r requirements.txt
3. Run migrations:
python manage.py migrate
4. Start the development server:
python manage.py runserver


## API Endpoints (Sample)

- `/api/home/` → Returns all homepage data (categories, sliders, best-selling, Apple Watches, footer poster, etc.)

## Author

Developed by **Soheil Jalili**.

