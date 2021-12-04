from django.shortcuts import render
from .serializers import InstructionsSerializer, PersonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from mainApps.models import Instructions, Person
# Create your views here.


class InstructionsViews(APIView):
	def get(self, request):
		instuctions = Instructions.objects.all()
		serializers = InstructionsSerializer(instuctions, many=True)
		return Response(serializers.data)


class InstructionsViews(APIView):
	def get(self, request):
		instuctions = Person.objects.all()
		serializers = PersonSerializer(instuctions, many=True)
		return Response(serializers.data)
