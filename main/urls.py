from venv import create
from django.urls import path
from . import views


urlpatterns = [
    path('' , views.base , name='base'),
    path('<int:id>/',views.detail,name='detail'),
    path('create',views.create, name='create'),
    path('edit/<int:id>/',views.edit, name='edit'),
    path('delete/<int:id>/',views.delete, name='delete'),
]