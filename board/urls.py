from django.urls import include, path
from rest_framework_nested import routers

from board.views import BoardViewSet, ColumnViewSet

router = routers.DefaultRouter()
router.register("boards", BoardViewSet)

boards_router = routers.NestedSimpleRouter(router, "boards", lookup="board")
boards_router.register("columns", ColumnViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(boards_router.urls)),
]
