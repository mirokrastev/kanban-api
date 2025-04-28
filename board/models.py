from django.db import models

from accounts.models import BaseUser
from base.models import BaseModel


class Board(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    slug = models.SlugField(blank=True, default="")

    owner = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name="boards")

    def __str__(self):
        return self.title


class Column(BaseModel):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="columns")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order"]


class Card(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    slug = models.SlugField(blank=True, default="")
    order = models.PositiveIntegerField(default=0)

    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name="cards")
    owner = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name="cards")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order"]
