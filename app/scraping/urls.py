from django.urls import path
from .views import KakaoMapScraper

urlpatterns = [
    path('execute/', KakaoMapScraper().scraping_view, name='scraping_view'),
]