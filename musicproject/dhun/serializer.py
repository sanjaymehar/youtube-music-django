from rest_framework import serializers
from .models import User,Album,Song

class Albumser(serializers.ModelSerializer):
    class Meta:
        models=Album
        fields='__all__'
        