from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from api.models import EmailAuth
from api.serializers import EmailAuthSerializer, EmailCodePairSerializer


class EmailAuthView(CreateAPIView):
    queryset = EmailAuth.objects.all()
    serializer_class = EmailAuthSerializer


class EmailCodeView(TokenObtainPairView):
    serializer_class = EmailCodePairSerializer
