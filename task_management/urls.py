from django.contrib import admin
from debug_toolbar.toolbar import debug_toolbar_urls
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

    path("tasks/", include("tasks.urls"),)
]+ debug_toolbar_urls()

# Ctrl + Shift + P   
