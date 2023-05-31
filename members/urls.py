from django.urls import path
from . import views        #. means current folder
urlpatterns=[
    path('index/',views.index,name='index'),
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]