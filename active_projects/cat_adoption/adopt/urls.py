from django.urls import path
from adopt import views

urlpatterns = [
    path("adopt/", views.temp_here, name="temp_here"),
    path("adopt/discover/", views.temp_somewhere, name="temp_somewhere"),
    path("adopt/search/", views.search_weather, name="search_weather"),
]
