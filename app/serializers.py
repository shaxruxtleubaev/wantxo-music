from rest_framework.serializers import *
from .models import Song

class SongSerializaer(ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'