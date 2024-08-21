from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer, UserSerializerWithoutID

@api_view(['GET'])
def getUsers(request):
  if request.method == 'GET':
    data = User.objects.all()

    serializer = UserSerializerWithoutID(data, many=True)
    return Response(serializer.data)
  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getUsersWithId(request):
  if request.method == 'GET':
    data = User.objects.all()

    serializer = UserSerializer(data, many=True)
    return Response(serializer.data)
  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getByID(request, id):
  try:
    data = User.objects.get(id=id)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)
  

  if request.method == 'GET':
    serializer = UserSerializerWithoutID(data)
    return Response(serializer.data)
  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getByDepartament(request, departament):
  try:
    data = User.objects.filter(departament=departament)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)
  

  if request.method == 'GET':
    serializer = UserSerializerWithoutID(data, many=True)
    return Response(serializer.data)
  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def createUser(request):
  if request.method == 'POST':
    new_user = request.data

    serializer = UserSerializerWithoutID(data=new_user)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateUser(request, id):
  try:
    data = User.objects.get(id=id)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'PUT':
    print(data)
    serializer = UserSerializerWithoutID(data, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteUser(request, id):
  try:
    data = User.objects.get(id=id)
    data.delete()
    return Response(status=status.HTTP_200_OK)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
