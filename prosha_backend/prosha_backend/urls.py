from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Core.urls')),
    path('', include('Shop.urls')),
    path('', include('News.urls')),
    path('', include('Article.urls')),
]
