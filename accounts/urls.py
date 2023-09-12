
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('page_logout/',views.page_logout, name='page_logout'),
    path('', views.accounts, name='accounts'),
]
