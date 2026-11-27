# BookMyService

**A full-stack service booking platform built with Django, JavaScript, and PostgreSQL.**

BookMyService is a web application that connects users with local service providers. Users can browse available services and submit booking requests, while service providers can create, manage, and respond to requests through their dashboards.

Originally developed as my CS50W Capstone project, BookMyService has since been deployed as a live web application. The project demonstrates full-stack development, database management, user authentication, role-based functionality, and production deployment.

## Live Demo

**Live Application:** https://bookmyservice-zhir.onrender.com/

## Demo

[![Watch the BookMyService demonstration](https://img.youtube.com/vi/A3saIEOI6hE/0.jpg)](https://youtu.be/A3saIEOI6hE)


## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** PostgreSQL (Neon)
- **Local Development Database:** SQLite
- **Deployment:** Render
- **Version Control:** Git and GitHub

## Features

### User Authentication
- User registration, login, and logout.
- Secure password handling through Django authentication.
- Separate user and service provider functionality.

### Service Management
- Providers can create and manage their service listings.
- Each service includes a name, description, and price.
- Users can browse available services.

### Booking System
- Users can submit booking requests for services.
- Booking requests are associated with the customer, provider, and selected service.
- Providers can accept or reject incoming requests.
- Booking statuses are tracked as Pending, Accepted, or Rejected.

### Dashboards and User Interface
- Separate dashboards for customers and service providers.
- Providers can manage their services and booking requests.
- Dynamic interface elements based on user roles and booking status.
- Flash messages and empty states for user feedback.
- Responsive layouts for desktop and mobile devices.

## Distinctiveness and Complexity

BookMyService differs from traditional e-commerce applications and other CS50W projects by focusing on service discovery and booking rather than products, shopping carts, and payments.

The application implements role-based functionality, allowing customers and service providers to interact with the platform differently. Customers can browse services and submit booking requests, while providers can create service listings and manage incoming requests.

The application uses multiple interconnected database models, including:

- **User:** Handles authentication and account information.
- **ProviderProfile:** Stores additional information about service providers.
- **Service:** Represents services offered by providers.
- **Booking:** Connects customers, providers, and services while tracking request status.

These relationships require careful handling of database operations and application logic to maintain consistency.

Additional complexity comes from handling different application states and edge cases, including preventing providers from booking their own services, managing booking statuses, and dynamically changing interface elements based on user roles and previous interactions.

The project also combines Django views and templates, JavaScript event handling, search functionality, responsive layouts, and conditional rendering into a single application.

Beyond the original development, I also deployed the application using Render and migrated its production PostgreSQL database to Neon. This involved configuring environment variables, managing database connections, creating database backups, and verifying the application after migration.

## Motivation

This project was inspired by a real-world problem I observed in India: finding reliable local service providers, such as domestic workers and independent service professionals, can be difficult despite the availability of affordable options.

After initially exploring this idea during a hackathon project, I decided to develop it further as my CS50W final project.

BookMyService aims to bridge this gap by providing a simple platform where users can discover and connect with local service providers more easily.

## Deployment and Database

BookMyService is deployed on Render, with Neon providing the production PostgreSQL database.

The deployment process involved:

- Configuring Django for production.
- Managing sensitive configuration through environment variables.
- Setting up Gunicorn as the application server.
- Configuring WhiteNoise for static file serving.
- Connecting Django to PostgreSQL using `DATABASE_URL`.
- Migrating the existing database and verifying application functionality.

The application uses SQLite as a fallback for local development and PostgreSQL in production.

## Project Structure

```text
BookMyService/
│
├── final/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── services/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── templates/
├── static/
├── manage.py
├── requirements.txt
├── build.sh
└── README.md
```

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/AA24107/BookMyService.git
cd BookMyService
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Future Improvements

- Prevent deletion of services with active bookings more robustly.
- Add watchlist functionality for users.
- Allow customers to book a service again if a previous request is rejected.
- Automatically clean up outdated booking requests.
- Improve UI/UX and introduce notifications.
- Implement a ratings and reviews system.
- Add a chat system for negotiating prices and scheduling after booking acceptance.

---

**Developed as my CS50W Capstone project.**
