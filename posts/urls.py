from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_post, name='create_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    
    # Search and Private Chat Routes
    path('search-users/', views.search_users, name='search_users'),
    path('chat/', views.chat_view, name='chat'),  # <--- Updated to match 'chat' in index.html
    path('chat/<str:username>/', views.chat_view, name='chat_user'),
]