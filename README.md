🏙️ Public Issue Reporting API

A Django REST API that allows citizens to report, view, and track public issues (like potholes, broken streetlights, or waste problems).
Admins can manage and mark issues as resolved, while citizens can upvote and comment on issues they care about.

🚀 Features

User registration & JWT authentication

Role-based access (citizen/admin)

Report issues with title, description, category, and location

Comment and upvote on issues

Filter issues by category, status, or location

Admin can mark issues as resolved

🧩 Tech Stack

Backend: Django REST Framework

Database: PostgreSQL

Authentication: JWT (djangorestframework-simplejwt)

Environment Management: python-decouple

Deployment: Render / Heroku

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/<your-username>/public-issue-reporting-api.git
cd public-issue-reporting-api

2️⃣ Create a virtual environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Setup environment variables

Create a .env file in the root folder:

DEBUG=True
SECRET_KEY=supersecretkey
DB_NAME=issue_reporting_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432

5️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Run the development server
python manage.py runserver

🔗 API Endpoints Overview
Method	Endpoint	Description
POST	/api/register/	Register new user
POST	/api/token/	Get JWT token
GET	/api/issues/	Get all issues
POST	/api/issues/	Create new issue
PATCH	/api/issues/{id}/resolve/	Resolve issue (admin)
POST	/api/issues/{id}/comments/	Add comment
POST	/api/issues/{id}/upvote/	Upvote an issue
🧱 Project Structure
issue_reporting_api/
│── config/
│── users/
│── issues/
│── comments/
│── upvotes/
│── .env
│── requirements.txt
│── README.md

🗓️ Development Plan

Week 1: Setup project, user model, authentication
Week 2: Issues, comments, upvotes
Week 3: Admin permissions, filters, extras
Week 4: Testing, docs, deployment

👨‍💻 Author

Solomon Ajohworode
Backend Developer @ ALX
🔗 GitHub
