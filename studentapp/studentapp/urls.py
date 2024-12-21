"""
URL configuration for studentapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
from django.contrib import admin
from django.urls import path, include
from .views import home  # Import the home view

urlpatterns = [
    path('', home, name='home'),  # This is the root URL
    path('admin/', admin.site.urls),
    path('to-do_list/', include('to_do_list.urls')),  # Connects to the to_do_list URLs
    path('blog/', include('blog.urls')),        # Connects to the blog URLs
    path('upload-notes/', include('upload_notes.urls')),  # Connects to the upload_notes URLs
]
"""
from django.contrib import admin
from django.urls import path, include
from . import views  # Import home view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home page URL
    path('', views.home, name='home'),

    # Blog app URLs
    path('blog/', include('blog.urls')),

    # To-Do List app URLs
    path('to-do/', include('to_do_list.urls')),

    # Upload Notes app URLs
    path('upload/', include('upload_notes.urls')),
]




