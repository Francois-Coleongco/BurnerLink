from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_link, name='create'),
    path('<slug:slug>/', views.redirect_link, name='redirect'),
]
