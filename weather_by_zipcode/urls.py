from django.urls import path
from weather_by_zipcode import views

urlpatterns = [
        path('', views.intro_page, name='intro_page'),
        path('weather/', views.weather_by_zipcode, name='weather_by_zipcode'),
]
