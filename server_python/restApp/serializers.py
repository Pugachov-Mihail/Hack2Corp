from rest_framework import serializers
from mainApps.models import Instructions, Office, Person, Posts


class InstructionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Instructions
		fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Posts
		fields = ('title', 'instuctions', 'allowance', 'allowance_level')

class OfficeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Office
		fields = "__all__"


class PersonSerializer(serializers.ModelSerializer):
	#instuction = InstructionsSerializer(many=True)
	post = PostSerializer(many=True)
	class Meta:
		model = Person
		fields = ("first_name", "first_name", "post", "allowance", "office")