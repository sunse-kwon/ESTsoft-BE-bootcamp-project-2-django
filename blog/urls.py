from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    path('write/', views.PostWrite.as_view(), name='write'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('edit/<int:pk>/', views.PostUpdate.as_view(), name='edit'),
    path('delete/<int:pk>', views.PostDelete.as_view(), name='delete'),
    path('<int:post_id>/comment/write/',
         views.CommentWrite.as_view(), name='cmt-write'),
    path('<int:comment_id>/comment/delete/',
         views.CommentDelete.as_view(), name='cmt-delete'),
    path('<int:post_id>/hashtag/write/',
         views.HashtagWrite.as_view(), name='tag-write'),
    path('<int:hashtag_id>/hashtag/delete/',
         views.HashtagDelete.as_view(), name='tag-delete'),
    path("search/<str:tag>/", views.PostSearch.as_view(), name='post-search'),
    path('<int:comment_id>/reply/write/',
         views.ReplyWrite.as_view(), name='reply-write'),
    path('<int:reply_id>/reply/delete/',
         views.ReplyDelete.as_view(), name='reply-delete'),
]
