from django.urls import path
from News import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('news', views.newsApi),
    path('news/<int:section>', views.newsApi),

    path('news/savefile', views.SaveFile),
    path('news/<slug:section>', views.newsApi),

    path('starnews', views.starnewsApi),
    path('starnews/<int:section>', views.starnewsApi),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
