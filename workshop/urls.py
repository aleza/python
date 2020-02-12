from django.urls import path

from . import views


app_name = 'workshop'

urlpatterns = [
    path('', views.index, name='index'),    
    path('cars/<int:owner_id>/', views.brands, name='brands'),
    path('cars/repairs/<int:owner_id>/', views.repairs, name='repairs'),
]