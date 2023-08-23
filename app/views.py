from django.shortcuts import render, redirect
from .models import Song
from .serializers import SongSerializaer
from rest_framework import viewsets, permissions

class SongViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Song.objects.all()
    serializer_class = SongSerializaer