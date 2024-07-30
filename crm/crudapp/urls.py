from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/',views.user_logout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('create/', views.create_record, name="create"),
    path('update/<int:pk>/', views.update_record, name="update"),
    path('view/<int:pk>',views.view_record, name="view"),
    path('delete/<int:pk>',views.delete_record, name="delete"),
]