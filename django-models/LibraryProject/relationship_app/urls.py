from django.urls import path
from .views import list_books
from .views import LoginView, LogoutView
from .templates import login, register,logout
from .views import register

urlpatterns = [
    path('books/', list_books, name='list_books'),
    # path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name= login), name = 'login'),
    path('logout/', LogoutView.as_view(template_name= logout), name = 'logout'),
    path('register/', register, name = 'register'),

]
