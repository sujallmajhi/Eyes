"""
URL configuration for project project.
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),
    
    # Home Page - shows all programs, talents, and team
    path('', views.home, name="home"),
    
    # Program Detail Page - shows specific details with 3 photos and 3 videos
    # The <int:pk> captures the ID from your card link (e.g., /program/1/)
    path('program/<int:pk>/', views.program_detail, name="program_detail"),
]

# Serving media files (images and videos) during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)