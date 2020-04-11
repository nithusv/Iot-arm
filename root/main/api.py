from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.authtoken.models import Token

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from .serializers import *

class UserAuthentication(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data = request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token , created = Token.objects.get_or_create(user=user)
        return Response(token.key)



class ModelList(APIView):
    def get(self,request):

        model = Mode.objects.all()
        serializer = ModeSerializer(model,many = True)
        return Response(serializer.data)

    def post(self,request):
        #model = Mode.objects.all()
        serializer = ModeSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ModelDetail(APIView):
    def get(self,request,model_id):
        try:
            model = Mode.objects.get(id = model_id)
        except Mode.DoesNotExist:
            return Response(f'Mode {model_id} not found', status= status.HTTP_404_NOT_FOUND)
        serializer = ModeSerializer(model)
        return Response(serializer.data)

    def put(self,request,model_id):
        try:
            model = Mode.objects.get(id = model_id)
        except Mode.DoesNotExist:
            return Response(f'Mode {model_id} not found', status= status.HTTP_404_NOT_FOUND)

        serializer = ModeSerializer(model,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,model_id):
        try:
            model = Mode.objects.get(id = model_id)
            model.delete()
            return Response(status= status.HTTP_410_GONE)
        except Mode.DoesNotExist:
            return Response(f'Mode {model_id} not found', status= status.HTTP_404_NOT_FOUND)




class OperationModelList(APIView):
    def get(self,request):

        operationmodel = OperationMode.objects.all()
        serializer = OperationModeSerializer(operationmodel,many = True)
        return Response(serializer.data)

    def post(self,request):
        #model = Mode.objects.all()
        serializer = OperationModeSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class OperationModelDetail(APIView):
    def get(self,request,object_type):
        try:
            model = OperationMode.objects.get(id = object_type)
        except OperationMode.DoesNotExist:
            return Response(f'Mode {object_type} not found', status= status.HTTP_404_NOT_FOUND)
        serializer = OperationModeSerializer(model)
        return Response(serializer.data)

    def put(self,request,object_type):
        try:
            model = OperationMode.objects.get(id = object_type)
        except OperationMode.DoesNotExist:
            return Response(f'Mode {object_type} not found', status= status.HTTP_404_NOT_FOUND)

        serializer = OperationModeSerializer(model,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,object_type):
        try:
            model = OperationMode.objects.get(id = object_type)
            model.delete()
            return Response(status= status.HTTP_410_GONE)
        except OperationMode.DoesNotExist:
            return Response(f'Mode {object_type} not found', status= status.HTTP_404_NOT_FOUND)
        


