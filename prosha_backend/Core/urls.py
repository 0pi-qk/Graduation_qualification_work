from django.urls import path
from Core import views

urlpatterns = [
    path('account', views.accountApi),
    path('account/<int:section>', views.accountApi),

    path('address', views.addressApi),
    path('address/<int:section>', views.addressApi),

    path('bird', views.birdApi),
    path('bird/<int:section>', views.birdApi),
    path('bird/<slug:section>', views.birdApi),
    path('bird/<slug:section>/<int:user>', views.birdApi),

    path('exchange', views.exchangeApi),
    path('exchange/<int:section>', views.exchangeApi),
]
