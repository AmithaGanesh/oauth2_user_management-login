
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
     
    path('admin/', admin.site.urls),
    path('',include('app.user_management.urls')),
    path('',include('app.loginapp.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]