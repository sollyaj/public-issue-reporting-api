from django.urls import path
from .views import (
    IssueListCreateView,
    IssueDetailView,
    ResolveIssueView,
    CommentCreateView,
    UpvoteToggleView
)

urlpatterns = [
    path('issues/', IssueListCreateView.as_view(), name='issue-list-create'),
    path('issues/<int:pk>/', IssueDetailView.as_view(), name='issue-detail'),
    path('issues/<int:pk>/resolve/', ResolveIssueView.as_view(), name='resolve-issue'),
    path('issues/<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
    path('issues/<int:pk>/upvote/', UpvoteToggleView.as_view(), name='upvote-toggle'),
]

