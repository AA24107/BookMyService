# BookMyService

A web application built using Django and JavaScript that allows users to browse and book local services, 
while service providers can create and manage their offerings.

This web application serves as an interface for small service providers to interact with users who need services. 

This project was developed as part of the CS50W Capstone and demonstrates full-stack web development 
including user authentication, dynamic UI updates, and role-based functionality.

This is my first full-stack project, and it focuses on building a complete booking workflow with 
role-based functionality and dynamic user interaction.


## Features

- User authentication (login, logout, register)
- Service creation and management by providers
- Booking system for users
- Clean and intuitive interface
- Role-based interface (different views for users and providers)
- Status tracking for bookings
- Dashboard for providers to manage services and track bookings
- Flash messages and empty states for better UX
- Responsive design for mobile and desktop


## Distinctiveness and Complexity

This project is distinct from other CS50W projects in several ways. Unlike the social network project, 
this application is focused on a service booking system with clear role separation between providers and 
users. Providers can create, edit, and manage services, while users can browse and request bookings. This 
role-based functionality introduces different interfaces and behaviors depending on the logged-in user, 
which was not present in earlier projects.

Additionally, this project is not a traditional e-commerce platform. Instead of handling products, carts,
and payments, the application focuses on service interactions and booking requests. The logic behind 
booking, tracking request status, and restricting actions based on user roles adds a different layer of 
complexity compared to standard e-commerce flows.

In terms of complexity, the application includes multiple interconnected models, including users, 
services, and booking requests. The relationships between these models required careful design to ensure 
data integrity and correct behavior across the application.

The project also implements dynamic user interfaces that change based on context. For example, users see 
booking options, providers see editing controls, and certain actions are disabled or modified depending 
on the current state (such as already requested services). This required conditional rendering both in 
Django templates and backend logic.

Additional complexity comes from handling edge cases, such as preventing providers from booking services, 
managing request states, and ensuring proper feedback through flash messages and empty states. These 
features improve usability while increasing the overall sophistication of the application.

This project also integrates multiple concepts introduced throughout the course, including search 
functionality, dynamic card-based layouts, status updates, interactive interfaces, Django templating, CSS 
styling, and JavaScript event handling. These components are combined into a single cohesive application 
rather than being implemented in isolation, increasing both the scope and integration complexity.

Overall, this project demonstrates a full-stack implementation that goes beyond the scope of previous 
assignments by combining role-based access, dynamic UI behavior, and a structured booking workflow.


## Motivation

This project was inspired by a real-world problem I observed in India — 
finding reliable local service providers (such as maids or small service workers) 
is often difficult, despite them offering more affordable options than larger companies.

After initially exploring this idea during a hackathon project, I found the concept 
interesting and decided to develop it further as my final project.

BookMyService aims to bridge this gap by providing a simple platform where users 
can discover and connect with local service providers more easily.


## Files and Structure

- `models.py` - Defines database models (User, Service, Booking)
- `views.py` - Handles application logic and request routing
- `urls.py` - Defines URL routes
- `templates/` - Contains HTML templates
- `static/` - Contains CSS and JavaScript files for front-end interactivity


## How to Run

1. Clone the repository
2. Run migrations:
```bash
python manage.py migrate
```
3. Start the server:
```bash
python manage.py runserver
```
4. Open the app in your browser


