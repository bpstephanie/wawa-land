from django.urls import path
from . import views

urlpatterns = [
     path('<slug:slug>/', views.event_detail, name='event_detail'),
     path('<slug:slug>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
     path('<slug:slug>/delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),
     path('', views.EventList.as_view(), name='event'),
]