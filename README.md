# Apple Store API Shop

This is a RESTful API built with Django and Django REST Framework for managing an Apple Store-like e-commerce backend.

## Features

- Product categories and listing
- Slider products for homepage
- Best-selling and featured products
- Apple Watch-specific product filtering
- Poster management (main and footer banners)
- Product detail endpoint added ✅
- Fully structured API responses for front-end integration
- Fully implemented cart management endpoints: support for retrieving, adding, removing, and clearing cart items

## Technologies

- Python
- Django
- Django REST Framework (DRF)
- SQLite / PostgreSQL (switchable)
- Git version control

## Getting Started

1. **Clone the repository:**

git clone https://github.com/soheil-jalili/Apple-Store-Api.git

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
- `/api/product/` → Handles product-related endpoints (list, detail, filtering, etc.)
- `/api/account/` → Handles user authentication and profile management (register, login, logout, etc.)
- `/api/cart/checkout/` → Retrieve all items in the authenticated user's cart (GET)
- `/api/cart/add/` → Add a product to the authenticated user's cart (POST)
- `/api/cart/remove/` → Remove a product from the authenticated user's cart (DELETE)
- `/api/cart/remove-all/` → Remove all items from the authenticated user's cart (DELETE)

## Author

Developed by **Soheil Jalili**.

