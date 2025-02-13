from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user-login/', views.user_login, name='user_login'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('add-room/', views.add_room, name='add_room'),
    path('add-user-to-room/<int:room_id>/', views.add_user_to_room, name='add_user_to_room'),
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
path('vacate-room/<int:room_id>/', views.vacate_room, name='vacate_room'),

]
