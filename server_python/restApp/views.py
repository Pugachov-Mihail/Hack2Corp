from django.shortcuts import render
from rest_framework import permissions

from .serializers import InstructionsSerializer, PersonSerializer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from mainApps.models import Instructions, Person


# Create your views here.


class InstructionsViews(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        instuctions = Instructions.objects.all()
        serializers = InstructionsSerializer(instuctions, many=True)
        return Response(serializers.data)


class CreatePerson(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = PersonSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            print(request.data)
            serializer.save(data=request.data)
            data['response'] = True
            return Response(data, status=201)
        else:
            data = serializer.errors
            return Response(data, status=400)
