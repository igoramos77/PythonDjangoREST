from django.urls import path, include
from django.contrib import admin

from rest_framework import routers


from aplic.api import viewsets as livrosviewsets

route = routers.DefaultRouter()

route.register(r'books', livrosviewsets.BooksViewSet, basename="Livros")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(route.urls))
]
