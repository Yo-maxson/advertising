from django.urls import path
from . import views

urlpatterns = [
    path('ads', views.GetAdvertInfoView.as_view()),
    path('ads_list',views.AdvertListAPIView.as_view()),
    path('ads_cr', views.AdvertCreateAPIView.as_view()),
]
