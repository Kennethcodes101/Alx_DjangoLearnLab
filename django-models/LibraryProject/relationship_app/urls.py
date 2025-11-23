from django.urls import path
from . import views
from .templates import login, logout
from django.urls import path
from relationship_app.views import admin_view
from relationship_app.views import librarian_view
from relationship_app.views import member_view


urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.LoginView.as_view(template_name= login ), name='login'),
    path('logout/', views.LogoutView.as_view(template_name= logout), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-dashboard/', admin_view, name='admin_view'),
    path('librarian-dashboard/', librarian_view, name='librarian_view'),
    path('member-dashboard/', member_view, name='member_view'),
]
