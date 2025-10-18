from django.urls import path
from . import views

urlpatterns = [
    path('issues/', views.IssueListCreateView.as_view(), name='issue-list-create'),
    path('issues/<int:pk>/', views.IssueDetailView.as_view(), name='issue-detail'),
    path('issues/<int:pk>/comment/', views.CommentCreateView.as_view(), name='comment-create'),
    path('issues/<int:pk>/resolve/', views.ResolveIssueView.as_view(), name='resolve-issue'),
    path('issues/<int:pk>/upvote/', views.UpvoteToggleView.as_view(), name='upvote-toggle'),
]


