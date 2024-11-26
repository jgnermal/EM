from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("index/", views.index, name="index"),
    path('employee/<int:id>/', views.view_employee, name='view_employee'),
    path("add/", views.add_employee, name='add_employee'),
    path('edit/employee/<int:id>/', views.edit_employee, name='edit_employee'),
    path('delete/employee/<int:id>/', views.delete_employee, name='delete_employee'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    
]
