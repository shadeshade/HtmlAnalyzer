import requests
from django.core.validators import URLValidator
from rest_framework import serializers

from core.helpers import get_random_string
from core.models import Task


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['url', ]

    def to_representation(self, instance):
        return {'identifier': instance.identifier}

    def create(self, validated_data):
        identifier = get_random_string()
        validated_data = {**validated_data, 'identifier': identifier, }
        return super(TaskCreateSerializer, self).create(validated_data)

    def validate_url(self, url):
        _url = url
        if 'http://' not in url and 'https://' not in url:
            _url = 'http://' + url
        url_validate = URLValidator()

        try:
            url_validate(_url)
        except:
            raise serializers.ValidationError("Please Enter a Valid URL")

        try:
            requests.get(_url)
        except:
            raise serializers.ValidationError("Server is not available")

        return url


class TaskRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['analyzed_data', ]

    def to_representation(self, instance):
        return instance.analyzed_data
