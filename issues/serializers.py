from rest_framework import serializers
from .models import Issue, Comment, Upvote

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author_name', 'text', 'created_at']


class IssueSerializer(serializers.ModelSerializer):
    reported_by_name = serializers.CharField(source='reported_by.username', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    upvote_count = serializers.IntegerField(source='upvotes.count', read_only=True)

    class Meta:
        model = Issue
        fields = [
            'id', 'title', 'description', 'category', 'status', 'location',
            'reported_by_name', 'created_at', 'updated_at', 'comments', 'upvote_count'
        ]
        read_only_fields = ['status', 'reported_by_name', 'created_at', 'updated_at', 'upvote_count']

    
    def create(self, validated_data):
        user = self.context['request'].user  # automatically assign logged-in user
        validated_data['reported_by'] = user
        return super().create(validated_data)



class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = ['id', 'issue', 'user', 'created_at']
