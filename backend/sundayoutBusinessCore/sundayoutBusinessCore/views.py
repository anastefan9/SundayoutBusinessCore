from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from authenticationBusiness.models import User
from django.shortcuts import get_object_or_404
from authenticationBusiness.serializers import UserSerializer 
from business.form import BusinessForm
from business.models import Business
from django.http import JsonResponse

@api_view(['POST'])
def login(request): 
    user = get_object_or_404(User, email = request.data['email'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."}, status = status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user = user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

@api_view(['POST'])
def signup(request): 
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.create(user = user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication #this allows us to authenticate sessions w a token
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request): 
    return Response("passed for {}".format(request.user.email)) 

@api_view(['POST'])
def create_business(request):
    form = BusinessForm(request.data, request.FILES)
    if form.is_valid():
        form.save()
        return Response({"message": "Business created successfully!"}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_businesses(request):
    data = Business.objects.all().values()
    dataList = list(data)
    for item in dataList:
            item['image'] = request.build_absolute_uri(item['image'])
    return JsonResponse(dataList, safe=False)