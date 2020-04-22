from rest_framework import viewsets
from  core.api.serializers import UserSerializers
from rest_framework.permissions import IsAuthenticated
from core.models import User


class CreateUserApi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsAuthenticated,)