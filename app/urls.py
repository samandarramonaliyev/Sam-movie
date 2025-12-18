from django.urls import path
from . import views


urlpatterns = [
    path("", views.films, name="films"),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('category/<int:pk>/', views.film_category, name='film-category'),
    path("film/<int:pk>/", views.film_detail, name='film-detail'),
    path('film/add/', views.add_film_view, name='film_add'),
]
