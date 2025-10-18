from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Issue, Comment, Upvote
from .serializers import IssueSerializer, CommentSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class IssueListCreateView(generics.ListCreateAPIView):
    queryset = Issue.objects.all().order_by('-created_at')
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)


class IssueDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResolveIssueView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        if not hasattr(request.user, 'role') or request.user.role != 'admin':
            return Response({'error': 'Only admin can mark as resolved.'}, status=403)
        issue.status = 'resolved'
        issue.save()
        return Response({'message': 'Issue marked as resolved.'})


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        issue = get_object_or_404(Issue, pk=self.kwargs['pk'])
        serializer.save(issue=issue, author=self.request.user)


class UpvoteToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        upvote, created = Upvote.objects.get_or_create(issue=issue, user=request.user)
        if not created:
            upvote.delete()
            return Response({'message': 'Upvote removed'})
        return Response({'message': 'Issue upvoted'})

