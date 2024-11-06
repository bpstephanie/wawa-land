from . import views
from django.urls import path

urlpatterns = [
    path('', views.EventList.as_view(), name='event'),
    path('<slug:slug>/', views.event_detail, name='event_detail'),
]