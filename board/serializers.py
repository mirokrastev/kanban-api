from rest_framework import serializers

from accounts.serializers import UserSerializer
from board.models import Board, Card, CardComment, Column


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ["id", "name", "order", "created_at", "updated_at"]


class CardSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Card
        fields = [
            "id",
            "name",
            "description",
            "slug",
            "order",
            "owner",
            "created_at",
            "updated_at",
        ]


class CardCommentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = CardComment
        fields = ["id", "comment", "owner", "created_at", "updated_at"]


class BoardSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    columns = ColumnSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = [
            "id",
            "name",
            "description",
            "slug",
            "owner",
            "columns",
            "created_at",
            "updated_at",
        ]
