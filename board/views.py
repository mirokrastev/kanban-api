from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response

from board.models import Board, Card, Column
from board.serializers import (
    BoardSerializer,
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

    @action(detail=True, methods=["post"])
    def columns_reorder(self, request, *args, **kwargs):
        ids = self.request.data.get("ids", [])

        id_order_map = {_id: inx for inx, _id in enumerate(ids)}

        board = self.get_object()
        columns = Column.objects.filter(board=board, id__in=ids)

        for column in columns:
            if column.id in id_order_map:
                column.order = id_order_map[column.id]

        Column.objects.bulk_update(columns, fields=["order"])

        return Response()


class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.prefetch_related("cards")
    serializer_class = ColumnSerializer

    def get_queryset(self):
        return Column.objects.filter(board_id=self.kwargs["board_pk"])

    def perform_create(self, serializer):
        serializer.save(board_id=self.kwargs["board_pk"])

    @action(detail=True, methods=["post"])
    def cards_reorder(self, request, *args, **kwargs):
        ids = self.request.data.get("ids", [])

        id_order_map = {_id: inx for inx, _id in enumerate(ids)}

        column = self.get_object()
        cards = Card.objects.filter(column=column, id__in=ids)

        for card in cards:
            if card.id in id_order_map:
                card.order = id_order_map[card.id]

        Card.objects.bulk_update(cards, fields=["order"])

        return Response()


class CardViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CardSerializer

    def get_queryset(self):
        return Card.objects.select_related("owner").filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
