from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from accounts import models, serializers


class RegisterView(CreateAPIView):
    queryset = models.BaseUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = ()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"status": "OK"}, status=status.HTTP_201_CREATED)
