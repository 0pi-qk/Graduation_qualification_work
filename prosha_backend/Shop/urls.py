from django.urls import path
from Shop import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('product', views.productApi),
    path('product/<int:section>', views.productApi),

    path('product/savefile', views.SaveFile),
    path('product/<slug:section>', views.productApi),
    path('product/<slug:section>/<int:user>', views.productApi),

    path('starproduct', views.starproductApi),
    path('starproduct/<int:section>', views.starproductApi),

    path('onlineorder', views.onlineorderApi),
    path('onlineorder/<int:section>', views.onlineorderApi),

    path('orderproduct', views.orderproductApi),
    path('orderproduct/<int:section>', views.orderproductApi),

    path('cart', views.cartApi),
    path('cart/<int:section>', views.cartApi),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
