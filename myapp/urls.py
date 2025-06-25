from django.urls import path
from . import views

urlpatterns = [
    path('telegram/webhook/', views.telegram_webhook, name='telegram_webhook'),
]
# myapp/urls.py
from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('telegram/webhook/', views.telegram_webhook, name='telegram_webhook'),
]
