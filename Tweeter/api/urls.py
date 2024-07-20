from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import (
    UserCreateView,
    TweetCreateView,
    CommentCreateView,
    UserFeedView,
    TweetFeedView,
    GetTweetView,
    TweetUpdateView,
    CommentUpdateView,
    CommentDeleteView,
    DeleteTweetView,
    ShowDeleteButton
)

urlpatterns = [
    # Tweet URLs
    path('tweets/', TweetFeedView.as_view(), name='tweet_feed'),
    path('tweets/create/', TweetCreateView.as_view(), name='tweet_create'),
    path('tweets/<int:pk>/', GetTweetView.as_view(), name='get_tweet'),
    path('tweets/<int:pk>/update/', TweetUpdateView.as_view(), name='update_tweet'),
    path('tweets/<int:pk>/delete/', DeleteTweetView.as_view(), name='delete_tweet'),
    path('tweets/<int:pk>/delete/', DeleteTweetView.as_view(), name='delete_tweet'),
    path('tweets/showDeleteButton',ShowDeleteButton.as_view(),name='show_delete_button'),

    # Comment URLs
    path('comments/create/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='update_comment'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),

    # User Feed URL
    path('user/feed/', UserFeedView.as_view(), name='user_feed'),
]
