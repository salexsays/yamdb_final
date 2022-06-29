from django.utils import timezone as dt

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from reviews.models import Category, Comment, Genre, Review, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ("id",)
        lookup_field = "slug"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ("id",)
        lookup_field = "slug"


class TitlePOSTSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(
        many=False, queryset=Category.objects.all(), slug_field="slug"
    )
    genre = SlugRelatedField(
        many=True, queryset=Genre.objects.all(), slug_field="slug"
    )

    class Meta:
        fields = "__all__"
        model = Title

    def validate_year(self, value):
        year = dt.now().year
        if not (value <= year):
            raise serializers.ValidationError("Проверьте год!")
        return value

    def validate_category(self, value):
        if Category.objects.filter(slug=value).exists():
            raise serializers.ValidationError(
                "Проверьте, что есть такая категория!"
            )
        return value

    def validate_genre(self, value):
        if Genre.objects.filter(slug=value).exists():
            raise serializers.ValidationError(
                "Проверьте, что есть такой жанр!"
            )
        return value


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        fields = (
            "id",
            "name",
            "year",
            "category",
            "genre",
            "description",
            "rating",
        )
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    title = serializers.SlugRelatedField(
        slug_field="id",
        read_only=True,
    )

    class Meta:
        fields = "__all__"
        model = Review

    def validate(self, data):
        title_id = self.context.get('view').kwargs.get('title_id')
        author = self.context["request"].user
        if (
            Review.objects.filter(author=author, title=title_id)
            and self.context["request"].method == "POST"
        ):
            raise serializers.ValidationError("Ваш отзыв уже есть!")
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )
    review = serializers.SlugRelatedField(
        slug_field="id",
        read_only=True,
    )

    class Meta:
        fields = "__all__"
        model = Comment
