# Django Internship Project – Telegram Bot Integration 🤖

This project is a Django-based internship system integrated with a Telegram bot (`@satyamintern_bot`) to interact with users.

## 💡 Features

- ✅ Django REST API setup
- ✅ JWT Authentication using `djangorestframework-simplejwt`
- ✅ Telegram Bot with polling support (`bot_polling.py`)
- ✅ Telegram Webhook (optional, via ngrok)
- ✅ Store Telegram user data (`TelegramUser` model)
- ✅ Celery-ready config (for task queues)

## 📁 Project Structure

django_internship_project/
│
├── backend/ # Django main settings & URLs
├── myapp/ # Telegram handlers and model
├── bot_polling.py # Starts bot with polling
├── db.sqlite3 # Database
├── manage.py
└── requirements.txt

markdown
Copy
Edit

## ⚙️ Setup Instructions

1. **Install dependencies**
pip install -r requirements.txt

markdown
Copy
Edit

2. **Apply migrations**
python manage.py makemigrations
python manage.py migrate

markdown
Copy
Edit

3. **Run development server**
python manage.py runserver

markdown
Copy
Edit

4. **Run Telegram bot (Polling)**
python bot_polling.py

markdown
Copy
Edit

5. **Test on Telegram**
Open Telegram and message your bot: [@satyamintern_bot](https://t.me/satyamintern_bot)

## 📦 Tech Stack

- Python 3
- Django 5.x
- Django REST Framework
- Telegram Bot (pyTelegramBotAPI)
- Celery (optional)
- SQLite

---

