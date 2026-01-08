from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.my_profile, name='my_profile'),
    path('change-avatar/', views.change_avatar, name='change_avatar'),
    path('u/<str:username>/', views.user_profile, name='user_profile'),  # 👈 YANGI

]


