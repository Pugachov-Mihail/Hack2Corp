from rest_framework import serializers
from mainApps.models import Instructions, Office, Person, Posts


class InstructionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Instructions
		fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Posts
		fields = "__all__"

class PersonSerializer(serializers.ModelSerializer):
	instuctions = InstructionsSerializer()
	post = PostSerializer()
	class Meta:
		model = Person
		fields = "__all__" #("first_name", "last_name", "instuctions", "post")