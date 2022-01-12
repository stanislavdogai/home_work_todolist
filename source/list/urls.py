from django.urls import path
from list.views import home_page, create, delete, task_view, update

urlpatterns = [
    path('', home_page, name='home_page'),
    path('create/', create, name='create'),
    path('delete/<int:pk>', delete, name='delete'),
    path('task/<int:pk>', task_view, name='view'),
    path('update/<int:pk>', update, name='update')
]