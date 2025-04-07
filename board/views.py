from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from board.models import Board, Card, CardComment, Column
from board.serializers import (
    BoardSerializer,
    CardCommentSerializer,
    CardSerializer,
    ColumnSerializer,
)


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.prefetch_related("cards")
    serializer_class = ColumnSerializer
    authentication_classes = ()
    permission_classes = ()

    def get_queryset(self):
        return Column.objects.filter(board_id=self.kwargs["board_pk"])

    def perform_create(self, serializer):
        serializer.save(board_id=self.kwargs["board_pk"])

    @action(detail=True, methods=["post"])
    def reorder(self, request, board_pk, pk=None):
        column = self.get_object()
        new_order = request.data.get("order")
        if new_order is not None:
            column.order = new_order
            column.save()
        return Response(self.get_serializer(column).data)


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_queryset(self):
        return Card.objects.filter(column_id=self.kwargs["column_pk"])

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["post"])
    def reorder(self, request, column_pk, pk=None):
        card = self.get_object()
        new_order = request.data.get("order")
        if new_order is not None:
            card.order = new_order
            card.save()
        return Response(self.get_serializer(card).data)


class CardCommentViewSet(viewsets.ModelViewSet):
    serializer_class = CardCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CardComment.objects.filter(card_id=self.kwargs["card_pk"])

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
