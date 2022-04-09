from django.urls import path
from . views import  Test_data


urlpatterns = [
    path('', Test_data.as_view()),
]