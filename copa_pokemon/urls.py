from django.contrib import admin
from django.urls import path, include

from jogos import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jogos.urls')),

]
