from django.urls import include, path
from rest_framework_nested import routers

from board.views import BoardViewSet, CardViewSet, ColumnViewSet

router = routers.DefaultRouter()
router.register("boards", BoardViewSet)

boards_router = routers.NestedSimpleRouter(router, "boards", lookup="board")
boards_router.register("columns", ColumnViewSet)

columns_router = routers.NestedSimpleRouter(boards_router, "columns", lookup="column")
columns_router.register("cards", CardViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(boards_router.urls)),
    path("", include(columns_router.urls)),
]
