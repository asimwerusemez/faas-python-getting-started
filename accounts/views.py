from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if User.objects.filter(username=email).exists():
        return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(username=email, email=email, password=password)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})

# Utiliser TokenObtainPairView pour la connexion
from rest_framework_simplejwt.views import TokenObtainPairView

class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)

