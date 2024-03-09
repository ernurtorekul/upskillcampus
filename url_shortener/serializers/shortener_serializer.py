from rest_framework import serializers
from shortener.models import URL

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['name', 'link', 'uuid']