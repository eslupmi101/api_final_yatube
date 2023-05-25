from rest_framework import serializers

from posts.models import Comment, Group, Post, Follow, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    group = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=Group.objects.all()
    )

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'image', 'group', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    created = serializers.DateTimeField(source='pub_date', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    def validate(self, data):
        following: str = data['following']

        if Follow.objects.filter(
            user=self.context['request'].user,
            following__username=following
        ).exists():
            raise serializers.ValidationError(
                {'detail': f'Вы уже подписаны на {following}.'}
            )

        return data

    def validate_following(self, following):
        user: str = self.context['request'].user
        following: str = following

        if user == following:
            raise serializers.ValidationError(
                {'detail': 'Нельзя подписаться на самого себя!'}
            )

        return following

    class Meta:
        model = Follow
        fields = ('user', 'following')
