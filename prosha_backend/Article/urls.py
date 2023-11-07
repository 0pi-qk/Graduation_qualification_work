from django.urls import path
from Article import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('article', views.articleApi),
    path('article/<int:section>', views.articleApi),

    path('article/savefile', views.SaveFile),
    path('article/<slug:section>', views.articleApi),

    path('stararticle', views.stararticleApi),
    path('stararticle/<int:section>', views.stararticleApi),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
