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
    post = PostSerializer(many=False)
    office = OfficeSerializer(many=False)
    password2 = serializers.CharField()
    email = serializers.EmailField()

    def save(self, **kwargs):
        user = Person(
            email=self.validated_data['email'],
            username=self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: "Пароли не совпадают"})
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = Person
        fields = ('username', 'password', 'password2', 'email', "first_name", "last_name", "post", "allowance", "office")


