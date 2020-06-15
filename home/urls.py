from django.urls import path
from . import views as home_views

urlpatterns=[
    path('', home_views.homePage, name = "homepage"),
    path('cars',home_views.carsPage, name="carspage"),
    path('team',home_views.teamPage,name="teampage")
]