
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wLook.urls')),
    path('', include('todo.urls')),
    path('', include('stocks.urls')),
    path('', include('courses.urls')),
]
