from django.urls import include, path
from rest_framework_nested import routers

from board.views import BoardViewSet, CardViewSet, ColumnViewSet

router = routers.DefaultRouter()
router.register("boards", BoardViewSet)
router.register("cards", CardViewSet, basename="cards")

boards_router = routers.NestedSimpleRouter(router, "boards", lookup="board")
boards_router.register("columns", ColumnViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("", include(boards_router.urls)),
]
