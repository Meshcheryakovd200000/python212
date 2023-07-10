from django.urls import path
from . import views

urlpatterns = [
    path('', views.repairs, name='repairs'),
    path('repair/<str:pk>/', views.repair, name='repair'),
]