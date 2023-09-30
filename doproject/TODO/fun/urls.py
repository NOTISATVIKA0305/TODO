from django.urls import path
from .views import home,add_client,delete_client,edit_client

urlpatterns = [
    path('',home,name='index'),
    path("add/", add_client, name='add'),
    path("delete/<int:id>/",delete_client, name='delete'),
    path("edit/<int:id>/",edit_client, name='edit'),

    
]