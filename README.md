Student Study Material Hub
A Django-based web application designed for students and educators to share, discover, manage, and download academic notes and study materials with secure user authentication and real-time chat features.

Key Features
User Authentication: Secure registration, login, and logout workflows to manage access control across the platform.

Study Material Management: Authenticated users can create posts, upload PDF notes, attach Google Drive or external document links, and delete their own posts.

Restricted File Downloads: Access control mechanisms ensuring that file downloads and direct PDF access are limited to logged-in users.

Real-Time Chat: Integrated messaging system allowing students to search for peers and communicate in real-time.

Admin Control: Built-in integration with the Django Admin panel for platform moderation and management.

Tech Stack
Backend: Python, Django

Frontend: HTML5, CSS3 (Responsive Design)

Database: SQLite (Development) / PostgreSQL-compatible (Production)

Deployment: Render Web Service

Local Development Setup
Follow these steps to set up and run the project locally on your machine.

1. Clone the Repository
Bash
git clone <your-repository-url>
cd <repository-folder>
2. Create and Activate a Virtual Environment
Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Apply Database Migrations
Bash
python manage.py makemigrations
python manage.py migrate
5. Create a Superuser (Optional, for Admin Panel)
Bash
python manage.py createsuperuser
6. Run the Development Server
Bash
python manage.py runserver
Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

Deployment on Render
This application is configured for deployment on Render as a Web Service.

Build Command: pip install -r requirements.txt && python manage.py migrate

Start Command: gunicorn blog.wsgi:application (or your project's WSGI path)

Environment Variables:

Ensure DEBUG is set to False in production.

Configure ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS to match your Render domain (https://<your-app-name>.onrender.com).

Media and Static Files: The URL configuration uses manual production serving via django.views.static.serve to ensure uploaded PDFs and static assets load correctly when DEBUG = False.
