from . import views
from django.urls import path


urlpatterns = [
     path('add_post/', views.add_post, name='add_post'),
     path('blog/', views.PostList.as_view(), name='blog'),
     path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
     path('blog/<slug:slug>/edit_comment/<int:comment_id>',
          views.comment_edit, name='comment_edit'),
     path('blog/<slug:slug>/delete_comment/<int:comment_id>',
          views.comment_delete, name='comment_delete'),
     path('delete_post/<int:post_id>',
          views.post_delete, name='post_delete'),
     path('profile/<str:username>/', views.user_profile, name='user_profile'),
     path('edit_post/<int:post_id>/', views.post_edit, name='post_edit'),
     path('', views.Home.as_view(), name='home'),

]
