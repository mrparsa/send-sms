from django.urls import path
from . import views

urlpatterns = [
    path('<int:a>/<str:y>/',views.send_sms , name = 'home'),
]
