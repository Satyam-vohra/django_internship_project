# django_internship_project
A Django-based internship portal integrated with Telegram Bot and JWT authentication. Includes user data handling, secure API endpoints, and polling/webhook support for Telegram interactions.


# 🧠 Django Internship Project

This is a full-stack internship management system built with **Django** and **Django REST Framework**, integrated with a **Telegram Bot**. It supports:

- ✅ User registration via Telegram bot commands (`/start`, etc.)
- ✅ JWT authentication for secure API access
- ✅ SQLite database integration
- ✅ Polling-based Telegram bot handling
- ✅ Option to switch to Webhook using NGROK
- ✅ Celery configured (with memory broker for testing)

## 📦 Tech Stack

- Django 5+
- Django REST Framework (DRF)
- Python 3.12
- SQLite
- Telegram Bot API (via pyTelegramBotAPI)
- Celery
- Ngrok (for webhook testing)

## 📁 Project Structure


django_internship_project/
├── myapp/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── ...
├── bot_polling.py
├── backend/
│ ├── settings.py
│ ├── urls.py
│ └── ...
└── requirements.txt

bash
Copy code

## 🚀 Getting Started

```bash
git clone https://github.com/your-username/django_internship_project.git
cd django_internship_project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python bot_polling.py
🤖 Telegram Bot Commands
/start – Welcomes the user

Replies with echo to any text message

User data stored in TelegramUser model

🛡 Security
JWT tokens are configured using SimpleJWT

CSRF disabled only for webhook view

Debug = False in production recommended


