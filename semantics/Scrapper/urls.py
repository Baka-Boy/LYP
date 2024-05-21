from django.contrib import admin
from django.urls import path, include
from Scrapper import views

urlpatterns = [
    path("", views.index, name='index'),
    path("scrapout", views.scrapout, name="scrapout"),
    path("textscrapout", views.textscrapout, name="textscrapout")
]