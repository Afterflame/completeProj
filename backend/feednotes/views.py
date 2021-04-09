from rest_framework import viewsets
from .models import Note
from django.contrib.auth.models import User
from .serializers import UserSerializer, NoteSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Note.objects.all().order_by('-date')
    serializer_class = NoteSerializer


@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        user = User.objects.create_user(
            request.data['username'],
            request.data['email'],
            request.data['password']
        )
        Token.objects.create(user=user)
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_user_by_token(request):
    try:
        user = Token.objects.get(key=request.data.get('mytoken')).user
    except:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    dict_obj = model_to_dict(user)
    return Response(dict_obj, status=status.HTTP_200_OK)