from django.urls import path
from . import views
from .templates import login, logout

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.LoginView.as_view(template_name= login ), name='login'),
    path('logout/', views.LogoutView.as_view(template_name= logout), name='logout'),
    path('register/', views.register, name='register'),
]
