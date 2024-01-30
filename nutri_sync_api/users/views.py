from rest_framework import generics, status
from .models import Users
from .serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password


class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response({'detail': 'Usuário criado com sucesso'}, status=status.HTTP_201_CREATED)


class AuthView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            return Response({'detail': 'Usuário não encontrado'}, status=status.HTTP_401_UNAUTHORIZED)

        if check_password(password, user.password):
            return Response({'detail': 'ok'})
        else:
            return Response({'detail': 'Senha incorreta'}, status=status.HTTP_401_UNAUTHORIZED)