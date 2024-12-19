from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),        # หน้าแรก (homepage1.html)
    path('next/', views.next_page, name='next_page'),  # หน้าถัดไป (homepage2.html)
]
