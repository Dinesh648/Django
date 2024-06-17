from django.contrib.auth.models import User
from rest_framework import serializers
#django serializes the python objects. From Developer perspective.
#dev just needs to write python code and Django automatically maps and performs the database operations.
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}
        #tells django to not give information about user when returning the user i.e no one can read the password.

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    #Django checks the model "User" and checks if all the fields are present and validated.
    #Once they are validated it is passed to create function as "validated_data" where we create the user.


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}