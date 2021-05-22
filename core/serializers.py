import requests
from django.core.validators import URLValidator
from rest_framework import serializers

from core.helpers import get_random_string, normalize_url
from core.models import Task
from core.tasks import analyze_html


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['url', ]

    def to_representation(self, instance):
        return {'identifier': instance.identifier}

    def create(self, validated_data):
        identifier = get_random_string()
        validated_data = {**validated_data, 'identifier': identifier, }
        task = super(TaskCreateSerializer, self).create(validated_data)
        analyze_html.delay(id=task.id)
        return task

    def validate_url(self, url):
        _url = normalize_url(url)
        url_validate = URLValidator()

        try:
            url_validate(_url)
        except:
            raise serializers.ValidationError("Please Enter a Valid URL")

        try:
            requests.get(_url)
        except requests.exceptions.RequestException as e:
            raise serializers.ValidationError(e)

        return url


class TaskRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['analyzed_data', ]

    def to_representation(self, instance):
        return instance.analyzed_data
