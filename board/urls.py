from django.urls import include, path
from rest_framework import routers

from board.views import BoardViewSet, CardViewSet, ColumnViewSet

router = routers.DefaultRouter()
router.register("boards", BoardViewSet)
router.register("columns", ColumnViewSet)
router.register("cards", CardViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
