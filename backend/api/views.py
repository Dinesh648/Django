from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer #needed to serialize the user data and in the back to manipulate db actions.
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author = user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author = self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author = user)

class CreateUserView(generics.CreateAPIView):
    # handles creating a new object for us
    queryset = User.objects.all() # here is the list of all the objects that we'll need to look when creating a new one so that we don't create if 
    # it already exists.

    serializer_class = UserSerializer # what kind of data we need to accept to make a new user. In this case a username and a password.
    permission_classes = [AllowAny] # who can actually call this class. Here we are giving access to anyone.


