from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from posts.models import Comment, Group, Post, Follow
from .paginations import CustomLimitOffsetPagination
from .serializers import (
    CommentSerializer, GroupSerializer,
    PostSerializer, FollowSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomLimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied(
                "You don't have permission to modify other users content."
            )
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied(
                "You don't have permission to modify other users content."
            )
        super(PostViewSet, self).perform_destroy(instance)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = None


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = None

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        return (Comment.objects.filter(
            post=self.get_post()
        ).select_related('post'))

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post()
        )

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied(
                "You don't have permission to modify other users content."
            )
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied(
                "You don't have permission to modify other users content."
            )
        super(CommentViewSet, self).perform_destroy(instance)


@permission_classes([IsAuthenticated])
class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    pagination_class = None
    filter_backends = [filters.SearchFilter]
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
