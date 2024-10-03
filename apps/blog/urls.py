from django.urls import path
from . import views

app_name="blog"

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/show/', views.show, name='show'),
]