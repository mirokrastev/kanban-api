from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('auth/', include([
        path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('register/', views.RegisterView.as_view(), name='register'),
    ])),
]
