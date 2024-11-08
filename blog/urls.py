from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]