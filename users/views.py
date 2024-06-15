# users/views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializer import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
