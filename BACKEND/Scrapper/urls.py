from django.urls import path, include
from Scrapper import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'scraper', views.getData)

urlpatterns = [
    path("api", views.getData, name='api'),
    path("chatcontent", views.getChatcontent, name='chatcontent'),
]