from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("astros/", include("astronauts.urls")),
    path("admin/", admin.site.urls),
]