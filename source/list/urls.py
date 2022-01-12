from django.urls import path
from list.views import home_page, create, delete

urlpatterns = [
    path('', home_page, name='home_page'),
    path('create/', create, name='create'),
    path('delete/<int:pk>', delete, name='delete')
]