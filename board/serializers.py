from rest_framework import serializers

from accounts.serializers import UserSerializer
from board.models import Board, Card, Column


class CardSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    column_id = serializers.PrimaryKeyRelatedField(
        source="column", write_only=True, required=False, queryset=Column.objects.all()
    )

    class Meta:
        model = Card
        fields = [
            "id",
            "title",
            "description",
            "slug",
            "order",
            "column_id",
            "owner",
            "created_at",
            "updated_at",
        ]


class ColumnSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Column
        fields = ["id", "title", "order", "created_at", "updated_at", "cards"]


class BoardSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    columns = ColumnSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = [
            "id",
            "title",
            "description",
            "slug",
            "owner",
            "columns",
            "created_at",
            "updated_at",
        ]
