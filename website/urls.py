from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("index/", views.index, name="index"),
    path('employee/edit/<int:id>/', views.edit_employee, name='edit_employee'),
    path('employee/delete/<int:id>/', views.delete_employee, name='delete_employee'),
    path('employee/view/<int:employee_id>/', views.view_employee, name='view_employee'),
    path("add/", views.add_employee, name='add_employee'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    
]
