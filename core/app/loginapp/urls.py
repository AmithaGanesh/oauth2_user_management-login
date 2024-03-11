from django.urls import path,include
from .views import LoginAPI, StudentAPI


urlpatterns = [
    path('login/', LoginAPI.as_view(), name='authentication-login'),
    path('student/', StudentAPI.as_view(), name='student-api'),]